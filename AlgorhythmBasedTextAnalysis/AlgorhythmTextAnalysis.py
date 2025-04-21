from collections import defaultdict
import pymorphy2
from AlgorhythmBasedTextAnalysis.LexicalSentimentAnalysis.Words.topic_keywords import topic_keywords

morph = pymorphy2.MorphAnalyzer(lang='uk')

class AlgorhythmTextAnalysis:
    def __init__(self, top_words_with_freq):
        """
        top_words_with_freq — список кортежів (слово, частота)
        """
        super().__init__()
        self.word_freqs = {morph.parse(word)[0].normal_form: freq for word, freq in top_words_with_freq}

    def run(self):
        topic_scores = defaultdict(int)

        # Проходимо по всіх темах і їх ключових словах
        for topic, keywords in topic_keywords.items():
            normalized_keywords = {morph.parse(k)[0].normal_form for k in keywords}
            for keyword in normalized_keywords:
                if keyword in self.word_freqs:
                    topic_scores[topic] += self.word_freqs[keyword]

        detected_topic = max(topic_scores, key=topic_scores.get) if topic_scores else "Невідомо"
        return detected_topic
