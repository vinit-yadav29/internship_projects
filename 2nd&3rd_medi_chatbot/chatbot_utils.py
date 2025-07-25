# chatbot_utils.py

import os
import pickle
import xml.etree.ElementTree as ET
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# 1. Load and parse XML data
def load_medquad_data(base_path):
    qa_pairs = []

    for root_dir, _, files in os.walk(base_path):
        for file in files:
            if file.endswith(".xml"):
                try:
                    tree = ET.parse(os.path.join(root_dir, file))
                    root = tree.getroot()
                    qa_section = root.find(".//QAPairs")

                    if qa_section is not None:
                        for pair in qa_section.findall("QAPair"):
                            question = pair.findtext("Question", "").strip()
                            answer = pair.findtext("Answer", "").strip()
                            if question and answer:
                                qa_pairs.append({"question": question, "answer": answer})
                except Exception as e:
                    continue

    return qa_pairs


# 2. QA Retriever class
class QARetriever:
    def __init__(self, qa_data):
        self.qa_data = qa_data
        self.questions = [pair["question"] for pair in qa_data]
        self.answers = [pair["answer"] for pair in qa_data]
        self.vectorizer = TfidfVectorizer()
        self.question_vectors = self.vectorizer.fit_transform(self.questions)

    def get_answer(self, user_question):
        user_vec = self.vectorizer.transform([user_question])
        sims = cosine_similarity(user_vec, self.question_vectors).flatten()
        best_idx = np.argmax(sims)

        if sims[best_idx] > 0.1:
            return self.answers[best_idx]
        else:
            return "Sorry, I couldn't find an answer to that question."


# 3. Save and load model
def save_model(retriever, path):
    with open(os.path.join(path, "qa_retriever.pkl"), "wb") as f:
        pickle.dump(retriever, f)

def load_model(model_path):
    with open(model_path, "rb") as f:
        return pickle.load(f)
