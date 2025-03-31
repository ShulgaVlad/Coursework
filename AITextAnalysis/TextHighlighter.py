import re
from PyQt6.QtGui import QTextCharFormat, QColor, QTextCursor
from NormalizeSentence import NormalizeSentence

class TextHighlighter:
    """Клас для виділення ключових речень у тексті."""

    @staticmethod
    def highlight_text(text_widget, original_text, main_sentences):
        """Виділяє головні речення зеленим кольором у текстовому полі."""
        text_widget.clear()

        format_ai = QTextCharFormat()
        format_ai.setForeground(QColor("green"))

        format_normal = QTextCharFormat()
        format_normal.setForeground(QColor("black"))

        cursor = text_widget.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.Start)

        main_sentences_list = [NormalizeSentence.normalize_sentence(s) for s in re.split(r'(?<=[.!?])\s+', main_sentences)]

        paragraphs = original_text.split("\n")
        for paragraph in paragraphs:
            sentences = re.split(r'(?<=[.!?])\s+', paragraph)
            for sentence in sentences:
                clean_sentence = NormalizeSentence.normalize_sentence(sentence)
                fmt = format_ai if clean_sentence in main_sentences_list else format_normal
                cursor.insertText(sentence + " ", fmt)
            cursor.insertText("\n")