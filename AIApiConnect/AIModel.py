from dotenv import load_dotenv
import os
import google.generativeai as genai

class AIModel:
    """Клас для взаємодії з API штучного інтелекту."""

    def __init__(self):
        load_dotenv()
        api_key = os.getenv("GOOGLE_AI_API_KEY")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def generate_response(self, prompt):
        """Відправляє запит до AIApiConnect та повертає відповідь."""
        try:
            response = self.model.generate_content(prompt)
            if response:
                return response.text
            else: "Помилка аналізу"
        except Exception as e:
            return f"Помилка: {str(e)}"
