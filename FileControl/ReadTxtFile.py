from PyQt6.QtWidgets import QFileDialog
import os
from docx import Document


class FileLoader:
    """Клас для завантаження тексту з файлу."""

    @staticmethod
    def load_text_from_file(widget):
        file_name, _ = QFileDialog.getOpenFileName(
            widget,
            "Виберіть файл",
            "",
            "Текстові файли (*.txt);;Word документи (*.docx);;Всі файли (*.*)"
        )
        if file_name:
            try:
                extension = os.path.splitext(file_name)[1].lower()
                if extension == ".txt":
                    with open(file_name, 'r', encoding='utf-8') as file:
                        return file.read()
                elif extension == ".docx":
                    return FileLoader._read_docx(file_name)
                else:
                    return "Непідтримуваний формат файлу."
            except Exception as e:
                return f"Помилка завантаження файлу: {str(e)}"

    @staticmethod
    def _read_docx(file_path):
        """Зчитування тексту з Word-документу."""
        doc = Document(file_path)
        return '\n'.join([para.text for para in doc.paragraphs])
