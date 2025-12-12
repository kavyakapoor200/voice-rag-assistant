from dotenv import load_dotenv
load_dotenv()

import os
import re
import streamlit as st
from groq import Groq

from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import InMemoryVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_groq import ChatGroq
from langchain_community.embeddings import HuggingFaceEmbeddings


# -------------------------------
# Load API key
# -------------------------------
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
if not GROQ_API_KEY:
    st.error(" Missing GROQ_API_KEY in .env")
    st.stop()

client = Groq(api_key=GROQ_API_KEY)


# -------------------------------
# Streamlit Page Setup
# -------------------------------
st.set_page_config(page_title="RAG Voice Assistant", page_icon="🎤", layout="centered")
st.title("🎤 RAG Voice Assistant")

# SESSION STATE for conversation history
if "history" not in st.session_state:
    st.session_state.history = []


# -------------------------------
# Folder setup
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIO_DIR = os.path.join(BASE_DIR, "audios")
os.makedirs(AUDIO_DIR, exist_ok=True)


# -------------------------------
# Models
# -------------------------------
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_db = InMemoryVectorStore(embeddings)

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model="llama-3.1-8b-instant"
)


# -------------------------------
# Helpers
# -------------------------------
def upload_audio(file):
    path = os.path.join(AUDIO_DIR, file.name)
    with open(path, "wb") as f:
        f.write(file.getbuffer())
    return path


def transcribe(file_path):
    """Groq Whisper transcription"""
    with open(file_path, "rb") as f:
        result = client.audio.transcriptions.create(
            file=("audio.mp3", f.read()),
            model="whisper-large-v3"
        )
    return result.text


def split_text(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    return splitter.split_text(text)


def clean(text):
    return re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()


def strict_rag_answer(question):
    """Answer ONLY based on uploaded audio"""
    docs = vector_db.similarity_search(question)

    if not docs:
        return "I don't know based on the audio."

    context = "\n\n".join([d.page_content for d in docs])
    prompt = ChatPromptTemplate.from_template(
        "Answer ONLY using this audio transcript. "
        "If answer is not in transcript, say: 'I don't know based on the audio." 
        "make answers bit big not super short'\n"
        "Context:\n{context}\n\nQuestion: {question}\nAnswer:"
    )
    chain = prompt | llm

    response = chain.invoke({"context": context, "question": question})
    answer = clean(response.content)

    # safety: if hallucination detected
    if "I think" in answer or "maybe" in answer:
        return "I don't know based on the audio."

    return answer


# -------------------------------
# UI — File Upload
# -------------------------------
uploaded = st.file_uploader("Upload an audio file (mp3/wav)", type=["mp3", "wav"])

if uploaded:
    file_path = upload_audio(uploaded)

    st.subheader("Transcribing audio… ⏳")
    transcript = transcribe(file_path)

    st.success("Transcription complete!")
    st.markdown("### 📝 Transcript")
    st.write(transcript)

    # Build RAG database
    chunks = split_text(transcript)
    vector_db.add_texts(chunks)

    st.divider()

    # -------------------------------
    # Chat Input
    # -------------------------------
    question = st.chat_input("Ask something about the audio…")
    
    if question:
        st.session_state.history.append(("user", question))

        answer = strict_rag_answer(question)
        st.session_state.history.append(("assistant", answer))

    # -------------------------------
    # Show Conversation History
    # -------------------------------
    st.subheader("💬 Conversation")

    for role, msg in st.session_state.history:
        if role == "user":
            st.chat_message("user").write(msg)
        else:
            st.chat_message("assistant").write(msg)

    st.caption("Strict RAG mode: answers only come from the audio transcript.")
