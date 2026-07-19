# 🤖 AI Knowledge Assistant

An intelligent document question-answering system built with **Django**, **Retrieval-Augmented Generation (RAG)**, **ChromaDB**, **Sentence Transformers**, and **Hugging Face Transformers**.

The application allows users to upload PDF documents, automatically process them into semantic embeddings, and ask natural language questions to receive AI-generated answers based on the uploaded content.

---

# 🚀 Features

- Upload PDF documents
- Extract text automatically
- Intelligent text chunking
- Semantic Embedding Generation
- ChromaDB Vector Database
- Semantic Search
- Retrieval-Augmented Generation (RAG)
- AI-powered Question Answering
- Multiple Document Support
- Chat History
- Source Chunk Display
- Prompt Engineering

---

# 🛠️ Technology Stack

Backend

- Python
- Django

AI

- Hugging Face Transformers
- Google FLAN-T5
- Sentence Transformers

Vector Database

- ChromaDB

Document Processing

- PyPDF

Text Processing

- LangChain Text Splitters

Database

- SQLite

Frontend

- HTML
- CSS
- Bootstrap
- JavaScript

---

# 📂 Project Structure

```text
AI-Knowledge-Assistant/

│
├── knowledge_base/
│   ├── views.py
│   ├── models.py
│   ├── forms.py
│   ├── rag.py
│   ├── llm.py
│   ├── embeddings.py
│   ├── chunking.py
│   ├── vector_store.py
│   ├── pdf_utils.py
│
├── media/
├── chroma_db/
├── requirements.txt
├── README.md
└── manage.py
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Knowledge-Assistant.git
```

Move into the project directory

```bash
cd AI-Knowledge-Assistant
```

Create virtual environment

```bash
python -m venv .venv
```

Activate virtual environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run migrations

```bash
python manage.py migrate
```

Run the server

```bash
python manage.py runserver
```

---

# 💡 How It Works

1. User uploads a PDF document.
2. Text is extracted using PyPDF.
3. Text is divided into semantic chunks.
4. Sentence Transformers generate embeddings.
5. Embeddings are stored in ChromaDB.
6. User asks a question.
7. Similar chunks are retrieved.
8. FLAN-T5 generates an answer using the retrieved context.
9. The system displays both the answer and the supporting source chunks.

---

# 🔮 Future Improvements

- User Authentication
- Conversation Memory
- Support for DOCX files
- Support for Multiple LLMs
- Streaming Responses
- OpenAI API Integration
- Image Question Answering
- Voice Interaction

---

# 👨‍💻 Author

**Fazil Ahmadi**

Django Developer | React Developer | Generative AI & RAG Developer

---

# ⭐ If you like this project, don't forget to star the repository.