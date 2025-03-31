import re

class NormalizeSentence:
    @staticmethod
    def normalize_sentence(sentence):
        """Очищає речення від зайвих пробілів та непотрібних символів."""
        return re.sub(r'\s+', ' ', sentence.strip().lower())