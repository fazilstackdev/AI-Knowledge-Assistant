# 🤖 AI Knowledge Assistant

An intelligent document question-answering system built with **Django**, **Retrieval-Augmented Generation (RAG)**, **ChromaDB**, **Sentence Transformers**, and **Hugging Face Transformers**.

The application allows users to upload PDF documents, automatically process them into semantic embeddings, and ask natural language questions to receive AI-generated answers based on the uploaded content.

---

## 🚀 Features

| Feature | Description |
|---------|-------------|
| 📄 **Upload PDF** | Upload PDF documents to the system |
| 📝 **Extract Text** | Automatically extract text from PDFs |
| ✂️ **Intelligent Chunking** | Divide text into semantic chunks |
| 🧠 **Semantic Embeddings** | Generate embeddings using Sentence Transformers |
| 🗄️ **ChromaDB Vector Store** | Store and manage embeddings in a vector database |
| 🔍 **Semantic Search** | Retrieve relevant chunks based on user queries |
| 🤖 **RAG (Retrieval-Augmented Generation)** | Combine retrieval and generation for accurate answers |
| 💬 **AI Question Answering** | Ask natural language questions and get AI-generated answers |
| 📚 **Multiple Document Support** | Upload and manage multiple documents simultaneously |
| 📜 **Chat History** | View and track previous conversations |
| 📖 **Source Chunk Display** | See the exact source chunks used to generate answers |
| ⚙️ **Prompt Engineering** | Optimized prompts for better AI responses |

---

## 🛠️ Technology Stack

### Backend
| Technology | Version |
|------------|---------|
| Python | 3.10+ |
| Django | 5.0+ |
| SQLite | Default |

### AI & Machine Learning
| Technology | Purpose |
|------------|---------|
| Hugging Face Transformers | AI model loading and inference |
| Google FLAN-T5 | Text generation (Question Answering) |
| Sentence Transformers | Generating semantic embeddings |

### Vector Database
| Technology | Purpose |
|------------|---------|
| ChromaDB | Storing and retrieving vector embeddings |

### Document Processing
| Technology | Purpose |
|------------|---------|
| PyPDF | Extracting text from PDF documents |

### Text Processing
| Technology | Purpose |
|------------|---------|
| LangChain Text Splitters | Dividing text into semantic chunks |

### Frontend
| Technology | Purpose |
|------------|---------|
| HTML5 | Page structure |
| CSS3 | Styling and responsive design |
| JavaScript | Interactive functionality |

---

## 📂 Project Structure

```text
AI-Knowledge-Assistant/
│
├── knowledge_base/                     # Main application directory
│   ├── views.py                        # Request handlers and UI rendering
│   ├── models.py                       # Database models
│   ├── forms.py                        # Form definitions
│   ├── rag.py                          # Retrieval-Augmented Generation logic
│   ├── llm.py                          # Language model interface
│   ├── embeddings.py                   # Embedding generation utilities
│   ├── chunking.py                     # Text chunking logic
│   ├── vector_store.py                 # ChromaDB vector store management
│   └── pdf_utils.py                    # PDF extraction utilities
│
├── media/                              # Uploaded files storage
├── templates/                          # HTML templates
├── chroma_db/                          # ChromaDB persistence directory
├── requirements.txt                    # Python dependencies
├── README.md                           # Project documentation
└── manage.py                           # Django management script
📸 Project Preview
🏠 Upload PDF
The system allows users to upload PDF documents, which are automatically processed into semantic chunks and stored in a vector database.

https://screenshots/home.png

🤖 AI Question Answering
Users can ask questions in natural language and receive AI-generated answers based on the uploaded document using Retrieval-Augmented Generation (RAG).

https://screenshots/chatbot.png

⚙️ Installation
Step 1: Clone the Repository
bash
git clone https://github.com/YOUR_USERNAME/AI-Knowledge-Assistant.git
Step 2: Navigate to Project Directory
bash
cd AI-Knowledge-Assistant
Step 3: Create Virtual Environment
bash
python -m venv .venv
Step 4: Activate Virtual Environment
Windows:

bash
.venv\Scripts\activate
Linux / Mac:

bash
source .venv/bin/activate
Step 5: Install Dependencies
bash
pip install -r requirements.txt
Step 6: Run Migrations
bash
python manage.py migrate
Step 7: Run the Server
bash
python manage.py runserver
Step 8: Access the Application
Open your browser and navigate to:

text
http://127.0.0.1:8000/
💡 How It Works
The diagram below illustrates the complete workflow of the AI Knowledge Assistant system:












Step-by-Step Explanation:
Step	Process	Description
1	Upload PDF	User uploads a PDF document to the system
2	Extract Text	PyPDF extracts raw text from the PDF
3	Chunking	LangChain divides text into overlapping semantic chunks
4	Generate Embeddings	Sentence Transformers convert chunks into vector embeddings
5	Store Vectors	ChromaDB stores embeddings for efficient retrieval
6	Ask Question	User submits a natural language question
7	Query Embedding	The question is converted into an embedding vector
8	Semantic Search	ChromaDB finds the most similar chunks
9	Context Retrieval	The retrieved chunks are used as context
10	Generate Answer	FLAN-T5 generates a response using the context
11	Display Output	System shows the answer with source references
🔮 Future Improvements
Priority	Feature	Description
⭐	User Authentication	Secure login and user-specific document management
⭐	Conversation Memory	Maintain chat history and context across sessions
⭐	DOCX Support	Support for Microsoft Word (.docx) files
⭐	Multiple LLMs	Support for different AI models (GPT, Claude, Llama, etc.)
⭐	Streaming Responses	Real-time streaming of AI-generated answers
🔸	OpenAI API Integration	Option to use GPT-3.5/4 models via API
🔸	Image Q&A	Answer questions based on images (multimodal AI)
🔸	Voice Interaction	Voice-based question asking and answer reading
👨‍💻 Author
Fazil Ahmadi

🔹 Role: Django Developer | React Developer | Generative AI & RAG Developer

🔹 Email: fazil2004.ah@gmail.com

🔹 GitHub: FazilAhmadi

⭐ Support
If you like this project, please consider:

⭐ Starring the repository on GitHub

🐛 Reporting any issues you encounter

🤝 Contributing to the project development

📄 License
This project is open-source and available under the MIT License.

Made with ❤️ by Fazil Ahmadi