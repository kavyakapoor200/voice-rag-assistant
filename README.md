# 🎙️ Voice-based RAG Assistant

A voice-enabled Retrieval-Augmented Generation (RAG) application that answers user queries **strictly from uploaded audio content**, ensuring accurate, hallucination-free responses using LLMs.

---

## 🚀 Overview

This project enables users to upload audio files, ask questions via voice or text, and receive reliable answers grounded only in the provided audio. It combines speech-to-text, semantic search, and LLM-based reasoning in an end-to-end pipeline.

---

## 🧠 Key Features

* Voice-based question answering from audio files
* Strict retrieval-only responses (no hallucinations)
* Multi-turn conversational support
* Fast semantic retrieval using vector embeddings
* Interactive web interface using Gradio

---

## 🛠️ Tech Stack

* **LLM**: LLaMA 3.1
* **Speech-to-Text**: Groq Whisper
* **RAG Framework**: LangChain
* **Vector Store**: InMemoryVectorStore
* **Embeddings**: Hugging Face
* **Frontend**: Gradio
* **Language**: Python

---

## ⚙️ System Architecture

1. User uploads an audio file
2. Audio is transcribed using Whisper
3. Transcription is chunked using recursive text splitting
4. Chunks are converted into embeddings
5. Relevant chunks are retrieved via similarity search
6. LLM generates answers strictly from retrieved context

---

## 🛡️ Hallucination Control

* Responses are generated **only from retrieved audio context**
* Queries outside the audio scope are safely rejected
* Session-based memory ensures contextual continuity without drifting

---

## 📊 Highlights

* Supports retrieval across **10+ semantic chunks per audio**
* Modular and extensible RAG pipeline
* Designed for reliability and domain adherence
* Suitable for knowledge assistants, education tools, and internal QA systems

---

## 🧪 Example Use Cases

* Audio-based knowledge assistants
* Lecture or meeting Q&A systems
* Podcast or interview analysis
* Voice-enabled document assistants

---

## 📦 Installation (Optional)

```bash
pip install -r requirements.txt
python app.py
```

---

## 📌 Future Improvements

* Persistent vector database (FAISS / Chroma)
* Speaker diarization
* Multilingual audio support
* Streaming audio input

---

## 🤝 Author

**Kavya Kapoor**
AI Engineer | Generative AI | RAG Systems

