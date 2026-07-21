![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-LCEL-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-Agentic--AI-FF6F61?style=for-the-badge&logo=langchain&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-412991?style=for-the-badge&logo=openai&logoColor=white)

# 🚀 Advanced RAG & Multi-Agent AI Bootcamp

Welcome to my **Retrieval-Augmented Generation (RAG) & Agentic AI** bootcamp repository! This repository serves as an end-to-end hands-on engineering record—progressing from foundational document ingestion, vector storage, and LCEL chains to advanced Agentic RAG, Vectorless RAG, GraphRAG, and production Multi-Agent architectures.

---

## 🛠 Tech Stack & Tools

* **Core Frameworks:** Python 3.13+, LangChain (Core, LCEL), LangGraph
* **Vector Stores & Indexes:** ChromaDB, FAISS, Graph Databases (Neo4j/Cypher), PageIndex
* **LLM & Embedding Models:** OpenAI (`gpt-4o-mini`, `text-embedding-3-small`), Groq (`llama-3.1-8b-instant`), Hugging Face CLIP (`clip-vit-base-patch32`)
* **Evaluation & Guardrails:** Ragas, TruLens, Guardrails AI
* **Environment & Package Management:** `uv`, PyTorch, PyMuPDF (`fitz`), Pillow

---

## 📂 Repository Structure & Curriculum

### 🟢 Completed Modules

#### 🔹 Module 1: Foundations of RAG, Vector Storage & Multimodal Ingestion (Sections 1–7)
* **`0-DataIngestionParsing.ipynb`**: Document loading, directory parsing, and advanced text splitting strategies (`RecursiveCharacterTextSplitter`).
* **`1-dataingestion.ipynb`**: Embedding generation, chunk management, and vector store setup using ChromaDB & FAISS.
* **`1b-chromadbLECL.ipynb`**: Native **LangChain Expression Language (LCEL)** construction using pipe operators (`|`), custom output parsers, prompt templates, hybrid search strategies, query enhancement, and conversational memory routing.
* **`multimodalrag.ipynb`**: **Multimodal PDF Ingestion**. Uses PyMuPDF to extract text & image bytes, generates unified multi-modal vector embeddings using **Hugging Face CLIP**, stores image data as Base64, and retrieves combined text-image context.

---

### 🔮 Upcoming Modules & Roadmap

#### 🔹 Module 2: Agent Foundations & Frameworks (Sections 8–10)
- [ ] **Section 08:** LangChain Hands-on V1
- [ ] **Section 09:** LangGraph Basics & State Management
- [ ] **Section 10:** Agents Architecture (Tools, Memory, Planning)

#### 🔹 Module 3: Advanced Agentic RAG Architectures (Sections 11–15)
- [ ] **Section 11:** Agentic RAG (Routing & Tool Calling)
- [ ] **Section 12:** Autonomous RAG
- [ ] **Section 13:** Multi-Agent RAG Systems
- [ ] **Section 14:** Corrective RAG (CRAG)
- [ ] **Section 15:** Adaptive RAG

#### 🔹 Module 4: High-Performance & Next-Gen Retrieval (Sections 16–18)
- [ ] **Section 16:** RAG with Persistent Memory
- [ ] **Section 17:** Cache RAG with LangGraph
- [ ] **Section 18:** Vectorless RAG with PageIndex (Reasoning-Based Retrieval)

#### 🔹 Module 5: Enterprise Governance & Gateway Infrastructure (Sections 19–20)
- [ ] **Section 19:** Guardrails & Safety Layers
- [ ] **Section 20:** LLM Gateways (Proxy, Fallbacks, Rate Limiting)

#### 🔹 Module 6: Knowledge Graphs & Evaluation (Sections 21–23)
- [ ] **Section 21:** Chatbot & RAG Evaluation (Ragas / TruLens Frameworks)
- [ ] **Section 22:** Introduction to Graph Databases & Cypher Query Language
- [ ] **Section 23:** GraphDB Practical Implementation with LangChain (GraphRAG)

#### 🔹 Module 7: Production Capstone (Section 24)
- [ ] **Section 24:** End-to-End Production Agentic RAG Project

---

## ⚙️ Quick Start & Environment Setup

This project uses **`uv`** for fast virtual environment and dependency management.

### 1. Clone the repository
```bash
git clone [https://github.com/jmhasan1/RAG-BootCamp.git](https://github.com/jmhasan1/RAG-BootCamp.git)
cd RAG-BootCamp