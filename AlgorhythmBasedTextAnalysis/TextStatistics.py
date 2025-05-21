import re
from collections import Counter
import pymorphy2
from AlgorhythmBasedTextAnalysis.LexicalSentimentAnalysis.Words.stopwords import stopwords

morph = pymorphy2.MorphAnalyzer(lang='uk')

class TextStatistics:
    def __init__(self):
        self.statistics_text = ""  # Ініціалізуємо поле для зберігання статистики

    def calculate_text_statistics(self, text):
        """Розраховує статистику тексту та виводить у UI, повертає набір топ-слів."""
        text = text.lower()  # Convert text to lowercase
        words = re.findall(r"\b[a-zа-яїєґ]+(?:['’][a-zа-яїєґ]+)?\b", text, re.UNICODE)  # Fix apostrophes
        unique_words = set(words)
        sentences = re.split(r'[.!?]', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        punctuation = re.findall(r'[.,!?;:]', text)
        # avg_word_length = sum(len(word) for word in words) / len(words) if words else 0
        # avg_sentence_length = sum(len(s.split()) for s in sentences) / len(sentences) if sentences else 0

        # Лематизуємо та фільтруємо службові слова
        lemmas = []
        for word in words:
            parsed = morph.parse(word)
            if not any('uk' in str(p.tag) for p in parsed) or parsed[0].score < 0.1:
                if word not in stopwords:
                    lemmas.append(word)
            else:
                # Якщо не технічний термін, лематизуємо
                normal_word = parsed[0].normal_form
                if normal_word not in stopwords:
                    lemmas.append(normal_word)

        # Підрахунок частоти лише після фільтрації
        word_frequencies = Counter(lemmas)

        sorted_frequencies = sorted(word_frequencies.items(), key=lambda item: item[1], reverse=True)
        top_words_str = ', '.join([f'{word} ({count})' for word, count in sorted_frequencies[:10]])

        self.statistics_text = (f"Кількість слів: {len(words)}\n"
                                f"Кількість унікальних слів: {len(unique_words)}\n"
                                f"Кількість речень: {len(sentences)}\n"
                                f"Кількість розділових знаків: {len(punctuation)}\n"
                                # f"Середня довжина слова: {avg_word_length:.2f}\n"
                                # f"Середня довжина речення: {avg_sentence_length:.2f}\n"
                                f"Топ 10 слів(приведених до нормальної форми): {top_words_str}")

        return words, sorted_frequencies    # Return set of top words
