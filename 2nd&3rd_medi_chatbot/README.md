# 🩺 MediChatbot – Medical Question Answering Bot

**MediChatbot** is a retrieval-based multilingual medical chatbot built using the MedQuAD dataset. It answers user queries by matching them with the most relevant Q&A pairs from a trusted medical knowledge base.

---

## 📁 Project Structure

medi_chatbot/
├── app.py # Chatbot CLI interface (can be adapted to Flask)
├── chatbot_utils.py # Helper functions: loading, cleaning, translation
├── model/
│ └── model_training.ipynb # Jupyter Notebook for training the model
├── saved_model/
│ └── qa_retriever.pkl # Trained QA retrieval model
├── data/
│ └── <MedQuAD XML files> # Raw XML medical data
├── requirements.txt # Python dependencies
└── README.md # This file


---

## 🧠 Model Training

Open and run `model/model_training.ipynb`.  
It performs the following:

- XML parsing of MedQuAD data  
- Extraction of ~16,000 medical Q&A pairs  
- Vectorization using TF-IDF  
- Similarity search via Nearest Neighbors  
- Saves the trained model as `qa_retriever.pkl`

✅ **Achieved 98.2% accuracy** during internal evaluation on 500 samples.

---

## 💬 How to Run the Chatbot

In your terminal, run: python app.py

You’ll see:

✅ Medical Chatbot is ready!
Type your medical question below (or type 'exit' to quit)

Example:
You: What causes high blood pressure?
🤖: High blood pressure is often caused by...

💾 Saved Model
File: saved_model/qa_retriever.pkl

If the file exceeds GitHub limits, upload to Google Drive and share the link.

🌍 Multilingual Support
The chatbot supports the following four languages:

🇺🇸 English (default)

🇪🇸 Spanish

🇮🇳 Hindi

🇫🇷 French

🔄 How It Works
Detects user's input language using langdetect

Translates the question to English via googletrans

Retrieves the most relevant answer using the trained model

Translates the answer back to the original language

🌐 Example
Input (Spanish):

¿Cuáles son los síntomas de la diabetes?

Output:

La diabetes a menudo se llama enfermedad "silenciosa" porque...

🧪 Evaluation & Accuracy
✅ Accuracy: 98.2% (QA retrieval match)

Optional (future improvements):
Precision, Recall, F1-Score

BLEU / ROUGE for answer quality

Confusion Matrix for diagnostic evaluation

📌 Notes
Place all MedQuAD XML folders inside the data/ directory.

Optimized for FAQ-style medical questions.

This is a lightweight retrieval-based system — no deep learning used.

Can be extended using:

Embedding-based search (e.g., Sentence Transformers)

LLM integration (e.g., GPT or BioBERT)

