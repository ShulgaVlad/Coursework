import re
# from collections import Counter
import pymorphy2

morph = pymorphy2.MorphAnalyzer(lang='uk')
class LexicalSentimentAnalysis:
    @staticmethod
    def load_words(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return set(word.strip().lower() for word in file.readlines())

    @staticmethod
    def tokenize(text):
        # Витягуємо тільки слова (без пунктуації), у нижньому регістрі
        return re.findall(r'\b\w+\b', text.lower())

    @staticmethod
    def lemmatize_words(words):
        return [morph.parse(word)[0].normal_form for word in words]

    @staticmethod
    def lexical_sentiment_analysis(text: str) -> str:
        words = LexicalSentimentAnalysis.tokenize(text)
        lemmas = LexicalSentimentAnalysis.lemmatize_words(words)

        # Використовуємо set для унікальних слів
        unique_lemmas = set(lemmas)
        # word_counts = Counter(lemmas)

        positive_words = LexicalSentimentAnalysis.load_words(
            'AlgorhythmBasedTextAnalysis/LexicalSentimentAnalysis/Words/positive_words.txt')
        negative_words = LexicalSentimentAnalysis.load_words(
            'AlgorhythmBasedTextAnalysis/LexicalSentimentAnalysis/Words/negative_words.txt')

        # Підрахунок для кожного унікального слова
        positive_matches = [word for word in unique_lemmas if word in positive_words]
        negative_matches = [word for word in unique_lemmas if word in negative_words]

        positive_count = len(positive_matches)
        negative_count = len(negative_matches)

        # print(f"Унікальні позитивні слова: {positive_matches}")
        # print(f"Унікальні негативні слова: {negative_matches}")
        # print(f"Позитивних: {positive_count}, Негативних: {negative_count}")

        # Тон залежить від різниці
        if positive_count - negative_count > 1:
            return "Позитивний"
        elif negative_count - positive_count > 1:
            return "Негативний"
        else:
            return "Нейтральний"
