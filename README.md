# 🚀 Advanced RAG & Multi-Agent Bootcamp

Welcome to my **Retrieval-Augmented Generation (RAG) & Agentic AI** bootcamp repository! This repository serves as a comprehensive, hands-on record of my journey through modern Generative AI engineering—moving from fundamental text chunking and vector storage to advanced LCEL chains, Multimodal processing, and Autonomous Multi-Agent architectures.

---

## 🛠 Tech Stack & Tools

* **Core Frameworks:** Python 3.13+, LangChain (Core, LCEL), LangGraph
* **Vector Stores & Indexes:** ChromaDB, FAISS
* **LLM & Embedding Providers:** OpenAI (`gpt-4o-mini`, `text-embedding-3-small`), Groq (`llama-3.1-8b-instant`), Hugging Face CLIP (`clip-vit-base-patch32`)
* **Environment & Package Management:** `uv`, PyTorch, PyMuPDF (`fitz`), Pillow

---

## 📂 Repository Structure & Curriculum

### 🔹 Module 1: Core Fundamentals & LCEL Pipeline
* **`0-DataIngestionParsing.ipynb`**: Document loading, directory parsing, and advanced text splitting strategies (`RecursiveCharacterTextSplitter`).
* **`1-dataingestion.ipynb`**: Embedding generation and vector store setup using ChromaDB.
* **`1b-chromadbLECL.ipynb`**: Native **LangChain Expression Language (LCEL)** construction. Implements modular pipe syntax (`|`), prompt templates, custom output parsers, and explicit memory routing.
* **`multimodalrag.ipynb`**: **Multimodal PDF Ingestion**. Uses PyMuPDF to extract text & image bytes, generates unified multi-modal vector embeddings using **Hugging Face CLIP**, stores image data as Base64, and retrieves combined text-image context.

---

### 🔮 Roadmap & Upcoming Modules

- [ ] **Section 08:** LangChain Hands-on V1
- [ ] **Section 09:** LangGraph Basics
- [ ] **Section 10:** Agents Architecture
- [ ] **Section 11:** Agentic RAG
- [ ] **Section 12:** Autonomous RAG
- [ ] **Section 13:** Multi-Agent RAG
- [ ] **Section 14:** Corrective RAG (CRAG)
- [ ] **Section 15:** Adaptive RAG
- [ ] **Section 16:** RAG with Persistent Memory
- [ ] **Section 17:** Cache RAG with LangGraph
- [ ] **Section 18:** Vectorless RAG with PageIndex
- [ ] **Section 19:** Guardrails & Safety
- [ ] **Section 20:** LLM Gateways
- [ ] **Section 21:** Chatbot & RAG Evaluation (Ragas / TruLens)
- [ ] **Section 22:** Intro to Graph Databases & Cypher Language
- [ ] **Section 23:** GraphDB Practical Implementation with LangChain (GraphRAG)
- [ ] **Section 24:** End-to-End Production Capstone Project

---

## ⚙️ Quick Start & Setup

This project uses **`uv`** for lightning-fast virtual environment and dependency management.

### 1. Clone the repository
```bash
git clone [https://github.com/jmhasan1/RAG-BootCamp.git](https://github.com/jmhasan1/RAG-BootCamp.git)
cd RAG-BootCamp