# 🚀 Internship Projects – NullClass July 2025

This repository contains my submissions for the **NullClass July 2025 data science Internship**. The tasks were completed between **02-07-2025 and 02-08-2025** as per the program requirements.

All source code, trained models, and notebooks are included or linked. Each project is organized in its own subfolder.

---

## 📁 Projects Included

### 1. 📝 Extractive Text Summarization
A tool that generates concise summaries by selecting and combining the most relevant sentences from the original text using extractive summarization techniques.

#### 🔧 Features:
- Uses TF-IDF and cosine similarity
- Ranks and selects top sentences
- Handles long documents
- Clean, modular implementation

---

### 2 & 3. 🩺 MediChatbot – Multilingual Medical Q&A Chatbot
 This project fulfills **both Task 2 and Task 3**.  
Project 3 is an **extension** of Project 2 and is implemented within the same solution.

#### 📌 Explanation:
- **Project 2:** Core medical chatbot using the MedQuAD dataset with English Q&A retrieval  
- **Project 3:** Enhances Project 2 by adding **multilingual support** (Spanish, Hindi, French) and **automatic language detection & translation**

#### 🔧 Features:
- Retrieval-based chatbot using TF-IDF + Nearest Neighbors
- Trained on 16,000+ medical Q&A pairs from MedQuAD
- Language detection using `langdetect`
- Automatic translation using `googletrans`
- CLI and Streamlit-based user interface

#### 🌍 Supported Languages:
- 🇺🇸 English (Default)
- 🇪🇸 Spanish
- 🇮🇳 Hindi
- 🇫🇷 French

#### 🧠 Performance:
- ✅ Accuracy: **98.2%** on internal test samples
- Model saved as `qa_retriever.pkl` (uploaded if small, or linked if large)

---


