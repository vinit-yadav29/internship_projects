import pickle
import os
from langdetect import detect
from deep_translator import GoogleTranslator

# Load the retriever model
model_path = "saved_model/qa_retriever.pkl"
if not os.path.exists(model_path):
    raise FileNotFoundError(f"❌ Model not found at: {model_path}")

with open(model_path, 'rb') as f:
    retriever = pickle.load(f)

print("✅ Medical Chatbot is ready!")
print("Type your medical question below (or type 'exit' to quit)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("👋 Goodbye!")
        break

    try:
        # Detect language
        lang = detect(user_input)

        # Translate to English if not already
        if lang != 'en':
            translated_input = GoogleTranslator(source='auto', target='en').translate(user_input)
        else:
            translated_input = user_input

        # Get answer in English
        answer_en = retriever.get_answer(translated_input)

        # Translate back to user's language
        if lang != 'en':
            final_answer = GoogleTranslator(source='en', target=lang).translate(answer_en)
        else:
            final_answer = answer_en

        print(f"🤖: {final_answer}")

    except Exception as e:
        print("⚠️ An error occurred:", e)
