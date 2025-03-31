import re
from collections import Counter

class TextStatistics:
    def __init__(self):
        self.statistics_text = ""  # Ініціалізуємо поле для зберігання статистики

    def calculate_text_statistics(self, text):
        """Розраховує статистику тексту та виводить у UI, повертає набір топ-слів."""
        text = text.lower()  # Convert text to lowercase
        words = re.findall(r"\b\w+(?:['’]\w+)?\b", text)  # Fix apostrophes
        unique_words = set(words)
        sentences = re.split(r'[.!?]', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        punctuation = re.findall(r'[.,!?;:]', text)
        avg_word_length = sum(len(word) for word in words) / len(words) if words else 0
        avg_sentence_length = sum(len(s.split()) for s in sentences) / len(sentences) if sentences else 0
        word_frequencies = Counter(words)
        top_words_list = word_frequencies.most_common(10)  # List of (word, count) tuples
        top_words = {word for word, _ in top_words_list}  # Set of top words for AlgorhythmTextAnalysis
        top_words_str = ', '.join([f'{word} ({count})' for word, count in top_words_list])

        self.statistics_text = (f"Кількість слів: {len(words)}\n"
                               f"Кількість унікальних слів: {len(unique_words)}\n"
                               f"Кількість речень: {len(sentences)}\n"
                               f"Кількість розділових знаків: {len(punctuation)}\n"
                               f"Середня довжина слова: {avg_word_length:.2f}\n"
                               f"Середня довжина речення: {avg_sentence_length:.2f}\n"
                               f"Топ 10 слів: {top_words_str}")

        return top_words  # Return set of top words