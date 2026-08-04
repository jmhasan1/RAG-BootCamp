# 🚀 Advanced RAG & Multi-Agent AI Bootcamp

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-LCEL-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-Agentic--AI-FF6F61?style=for-the-badge&logo=langchain&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-412991?style=for-the-badge&logo=openai&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging_Face-Transformers-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)

Welcome to my **Retrieval-Augmented Generation (RAG) & Agentic AI** bootcamp repository! This repository serves as an end-to-end hands-on engineering record—progressing from foundational document ingestion, vector storage, and LCEL chains to advanced Agentic RAG, Vectorless RAG, GraphRAG, and production Multi-Agent architectures.

---

## 🛠 Tech Stack & Tools

* **Core Frameworks:** Python 3.13+, LangChain (Core, LCEL), LangGraph
* **Vector Stores & Indexes:** ChromaDB, FAISS, DataStax AstraDB, Pinecone, Graph Databases (Neo4j/Cypher), PageIndex
* **LLM & Embedding Models:** OpenAI (`gpt-4o-mini`, `text-embedding-3-small`), Groq (`llama-3.1-8b-instant`), Hugging Face CLIP (`clip-vit-base-patch32`)
* **Evaluation & Guardrails:** Ragas, TruLens, Guardrails AI
* **Environment & Package Management:** `uv`, PyTorch, PyMuPDF (`fitz`), Pillow, Pydantic, SQLite3

---

## 📂 Repository Structure & Curriculum

### 🟢 Completed Modules

#### 🔹 Module 1: Foundations of RAG, Vector Storage & Multimodal Ingestion (Sections 1–7)

* **`0-DataIngestionParsing/`**: Multi-format data loading and parsing pipelines.
  * `1-dataIngestion.ipynb`: Fundamental data ingestion techniques.
  * `2-dataParsingpdf.ipynb`: PDF parsing and document loading.
  * `3-dataParsigdoc.ipynb`: DOCX/Word document parsing.
  * `4-csvEXcelParsing.ipynb`: Structured CSV and Excel dataset processing.
  * `5-jsonParsing.ipynb`: JSON parsing and nested key-value extraction.
  * `6-DatabaseParsing.ipynb`: Relational database connections and SQL data extraction.
* **`1-VectorEmbeddingandDatabases/`**: Embedding generation algorithms.
  * `embedding.ipynb`: Open-source and Hugging Face embedding pipelines.
  * `openAIembeddings.ipynb`: OpenAI embedding models (`text-embedding-3-small/large`).
* **`2-VectorStores/`**: Local and self-hosted vector database integration.
  * `1a-chromadb.ipynb`: ChromaDB initialization, collection creation, and similarity search.
  * `1b-chromadbLECL.ipynb`: Native **LangChain Expression Language (LCEL)** chaining with ChromaDB.
  * `2-faiss.ipynb`: In-memory similarity search with FAISS index management.
  * `3-OtherVectorStores.ipynb`: Additional vector store abstractions and comparisons.
* **`3-VectorDatabases/`**: Managed cloud vector databases.
  * `Datastaxdb.ipynb`: Serverless Cassandra/AstraDB vector search integration.
  * `PineconeVectorDB.ipynb`: Managed cloud vector indexing with Pinecone.
* **`4-Advanced Chunking & Processing/`**: Advanced text splitting algorithms.
  * `SemanticChunking.ipynb`: Context-aware semantic chunking based on embedding distance thresholds.
* **`5-Hybrid Search Strategies/`**: Combined retrieval techniques.
  * `1-DenseSparseSearch.ipynb`: Hybrid dense (embeddings) + sparse (BM25) search.
  * `2-Reranking.ipynb`: Cross-encoder reranking to improve top-k context precision.
  * `3-mmr.ipynb`: Maximal Marginal Relevance (MMR) for diversity in retrieved contexts.
* **`6-Query Enhancement/`**: Advanced pre-retrieval query transformation techniques.
  * `1-QueryExpansion.ipynb`: Multi-query generation and query expansion via LLMs.
  * `2-querydecomposition.ipynb`: Decomposing complex queries into sub-queries.
  * `3-HyDE.ipynb`: Hypothetical Document Embeddings (HyDE) zero-shot retrieval.
* **`7-MultliModalRAGIntroduction/`**: Processing unstructured multimodal inputs.
  * `multimodalrag.ipynb`: Extracting text and image bytes using PyMuPDF, generating joint vector embeddings with Hugging Face CLIP, storing image Base64 payloads, and retrieving multi-modal contexts.

---

#### 🔹 Module 2: Agent Foundations & Frameworks (Sections 8–10)

* **`8-LangChain Hands-on V1/`**: Foundations of LangChain development.
  * `1-langchainintro.ipynb`: Core concepts, primitives, and prompt template construction.
  * `2-modelintegration.ipynb`: Integrating and swapping ChatOpenAI, Groq, and Hugging Face LLMs.
  * `3-tools.ipynb`: Defining custom function tools and `@tool` decorators.
  * `4-messages.ipynb`: System, Human, and AI message state management and history routing.
  * `5-structuredoutput.ipynb`: Forcing structured JSON/Pydantic model responses from LLMs.
  * `6-middleware.ipynb`: Middleware handlers, interceptors, and custom chain logic.
* **`9-LangGraph Basics/`**: Cyclic stateful orchestration with LangGraph.
  * `1-simplegraph.ipynb`: Defining nodes, edges, state dictionaries, and simple execution paths.
  * `2-chatbot.ipynb`: Building conversational stateful graph networks.
  * `3-DataclassStateSchema.ipynb`: Typing agent state using Python `@dataclass`.
  * `4-pydantic.ipynb`: Enforcing strict runtime state validation via Pydantic schemas.
  * `5-ChainsLangGraph.ipynb`: Connecting LCEL runnables and chains inside LangGraph nodes.
  * `6-chatbotwithmultipletools.ipynb`: Building a multi-tool ReAct graph with conditional routing.
* **`10-Agent Architeture/`**: Production agent patterns & execution runtimes.
  * `ReActAgents.ipynb`: Implementing Reason + Act (ReAct) looping architectures.
  * `streaming.ipynb`: Token-by-token and node-by-node output streaming from agent states.
  * `Debugging/`: Server setup, state checkpointing (`.pckl`), and API monitoring using `openai_agent.py` and `langgraph.json`.

---

### 🔮 Upcoming Modules & Roadmap

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