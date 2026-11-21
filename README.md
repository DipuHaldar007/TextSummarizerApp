# 🚀 Text Summarizer Using T5 Transformer

An AI-powered Text Summarization Web Application built using **Python, Hugging Face Transformers, T5-Small, PyTorch, and FastAPI**.

This application takes lengthy text as input and generates a concise, meaningful summary using a pre-trained T5-Small Transformer model.

## 📌 Project Overview

Text Summarization is an important Natural Language Processing (NLP) task that reduces lengthy documents into shorter versions while preserving their essential information.

This project uses the **T5-Small (Text-to-Text Transfer Transformer)** architecture to perform automatic text summarization through an interactive web application.

## ✨ Features

- 🤖 AI-powered automatic text summarization.
- 🧠 T5 Transformer model integration.
- 📝 Text preprocessing and cleaning.
- ⚡ FastAPI backend for handling API requests.
- 🎨 Interactive frontend using HTML, CSS, and JavaScript.
- 🔥 PyTorch-based model inference.
- 💻 GPU acceleration support when available.
- 📄 REST API for text summarization.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| T5-Small Transformer | Text summarization |
| Hugging Face | Pre-trained model and tokenizer |
| PyTorch | Deep learning framework |
| FastAPI | Backend API development |
| HTML | Frontend structure |
| CSS | Frontend styling |
| JavaScript | Frontend interaction |

## 🧠 Model Information

- **Model Architecture:** T5-Small (Text-to-Text Transfer Transformer)
- **Framework:** Hugging Face Transformers
- **Deep Learning Framework:** PyTorch
- **Model Repository:** [Deptendra7/text-summarizer-t5](https://huggingface.co/Deptendra7/text-summarizer-t5)

The model is loaded directly from Hugging Face using the Transformers library.

## 📂 Project Structure

```text
TextSummarizerApp/
│
├── app.py                  # FastAPI backend
├── index.html              # Frontend interface
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
├── LICENSE                 # MIT License
├── .gitignore              # Ignored files
│
└── text_summarizer.ipynb   # Text summarizer main file
```

## ⚙️ Installation and Setup

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/DipuHaldar007/TextSummarizerApp.git
```

### 2. Navigate to the Project Directory

```bash
cd TextSummarizerApp
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

Install SentencePiece if required:

```bash
pip install sentencepiece
```

### 5. Run the Application

```bash
uvicorn app:app --host 127.0.0.1 --port 8000
```

### 6. Open the Application

Visit the following URL in your browser:

```text
http://127.0.0.1:8000
```

## ⚠️ Important Notes

- The T5 model is downloaded from Hugging Face when the application starts for the first time.
- An active internet connection is required for the initial model download.
- Input text is tokenized with a maximum input length of 512 tokens.
- Longer input text is truncated by the current implementation.
- Model inference time depends on your hardware and available resources.

## 🚀 Future Improvements

- [ ] Deploy the application publicly.
- [ ] Add PDF and document summarization.
- [ ] Support multiple summarization options.
- [ ] Improve the user interface.
- [ ] Add support for longer documents.
- [ ] Optimize model inference performance.

## 👨‍💻 Author

**Deptendra Haldar**

B.Tech CSE (AI & ML) Student | Aspiring AI Engineer

Interested in Artificial Intelligence, Machine Learning, Deep Learning, and Natural Language Processing.

- GitHub: [DipuHaldar007](https://github.com/DipuHaldar007)

⭐ If you find this project interesting, consider giving the repository a star!

**Building, Learning, and Exploring AI! 🚀**
