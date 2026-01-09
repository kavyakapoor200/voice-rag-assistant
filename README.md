# 🎤 Voice-Based RAG Assistant

A production-style **Voice Retrieval-Augmented Generation (RAG)** system that answers user questions **strictly from uploaded audio content**, ensuring **hallucination-free responses** using LLMs.

🔗 **Live Demo**: Hugging Face Spaces (link in About section)

---

## 📌 What This Project Does

Users upload an audio file (lecture, meeting, podcast, etc.) and ask questions via text.
The system **transcribes the audio**, retrieves relevant context, and generates answers **only from the audio**, refusing to guess when information is missing.

---

## 🚀 Key Features

* 🎧 Audio-based question answering
* 🧠 Retrieval-Augmented Generation (RAG)
* 🛡️ Strict hallucination control
* 🔁 Multi-turn conversational support
* ⚡ Fast semantic search using embeddings
* 🌐 Deployed interactive UI

---

## 🧠 How It Works (Simple Flow)

```
Audio Upload
   ↓
Speech-to-Text (Whisper)
   ↓
Text Chunking
   ↓
Embeddings Generation
   ↓
Vector Store (Similarity Search)
   ↓
LLM Answer (Strictly from Audio)
```

---

## 🛠️ Tech Stack

* **Language**: Python
* **LLM**: LLaMA 3.1 (via Groq)
* **Speech-to-Text**: Whisper (Groq)
* **RAG Framework**: LangChain
* **Embeddings**: Hugging Face (MiniLM)
* **Vector Store**: In-Memory Vector Store
* **UI**: Gradio
* **Deployment**: Hugging Face Spaces

---

## 🛡️ Hallucination Control

* The LLM is prompted to **answer only from retrieved transcript chunks**
* If relevant context is missing, the system replies:

  > *“I don’t know based on the audio.”*
* Additional safety checks block speculative responses

This makes the system suitable for **enterprise, education, and internal knowledge tools**.

---

## 📦 Installation (Run Locally)

### 1️⃣ Clone the repository

```bash
git clone https://github.com/kavyakapoor200/voice-rag-assistant.git
cd voice-rag-assistant
```

---

### 2️⃣ Create & activate virtual environment (recommended)

```bash
python -m venv venv
```

**Windows**

```bash
venv\Scripts\activate
```

**Mac / Linux**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Set environment variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key
```

---

### 5️⃣ Run the application

```bash
python app.py
```

The Gradio interface will open in your browser.

---

## 🧪 Testing

Sample audio files are included in the `audios/` directory for quick testing.
Upload an audio file and start asking questions.

---

## 🎯 Why This Project Matters

Most LLM assistants hallucinate.
This project demonstrates how **RAG systems can ground LLM responses in real data**, making AI outputs reliable, explainable, and production-ready.

---

## 📚 Key Learnings

* Designing end-to-end RAG pipelines
* Preventing hallucinations in LLM applications
* Semantic search with embeddings
* Building and deploying AI systems
* Separating UI and backend logic for scalability

---

## 🔮 Future Improvements

* Persistent vector databases (FAISS / ChromaDB)
* Multi-language audio support
* Streaming audio input
* Speaker diarization

---

## 👩‍💻 Author

**Kavya Kapoor**
AI Engineer | Generative AI | RAG Systems

---
