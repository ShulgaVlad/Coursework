from PyQt6.QtWidgets import QFileDialog

class FileLoader:
    """Клас для завантаження тексту з файлу."""
    @staticmethod
    def load_text_from_file(widget):
        file_name, _ = QFileDialog.getOpenFileName(widget, "Виберіть файл", "", "Текстові файли (*.txt);;Всі файли (*.*)")
        if file_name:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    return file.read()
            except Exception as e:
                return f"Помилка завантаження файлу: {str(e)}"