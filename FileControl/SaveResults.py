from PyQt6.QtWidgets import QFileDialog, QMessageBox
import zipfile
import os


class SaveResults:
    @staticmethod
    def save(text_input,
             result_text_specialization_output,
             result_text_algorhythm_specialization_output,
             result_text_tone_output,
             result_main_sentence_output,
             statistics_text,
             zipf_image_path="zipf_plot.png"):
        """Зберігає результати аналізу у текстовий файл із додаванням графіка Zipf."""
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(text_input, "Зберегти результат", "",
                                                   "ZIP Files (*.zip);;Text Files (*.txt)")

        if file_path:
            try:
                if file_path.endswith(".zip"):
                    # Створюємо ZIP-архів
                    with zipfile.ZipFile(file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                        # Створюємо тимчасовий текстовий файл із результатами
                        text_content = (
                                "Результати аналізу тексту:\n\n"
                                "Спеціалізація(ШІ):\n" + result_text_specialization_output.toPlainText() + "\n\n"
                                "Спеціалізація(Алгоритмічна):\n" + result_text_algorhythm_specialization_output.toPlainText() + "\n\n"
                                "Тон тексту:\n" + result_text_tone_output.toPlainText() + "\n\n"
                                "Найголовніші речення:\n" + result_main_sentence_output.toPlainText() + "\n\n"
                                "Статистика тексту:\n" + statistics_text + "\n"
                                "Графік Zipf доступний у zipf_plot.png у цьому архіві."
                        )
                        with open("temp_results.txt", "w", encoding="utf-8") as temp_file:
                            temp_file.write(text_content)
                        zipf.write("temp_results.txt", "results.txt")
                        if os.path.exists(zipf_image_path):
                            zipf.write(zipf_image_path, "zipf_plot.png")
                        os.remove("temp_results.txt")  # Видаляємо тимчасовий файл
                    QMessageBox.information(text_input, "Збережено", "Результати успішно збережено у ZIP-архів.")
                else:
                    # Зберігаємо лише текстовий файл із посиланням на зображення
                    with open(file_path, "w", encoding="utf-8") as file:
                        file.write(
                            "Результати аналізу тексту:\n\n"
                            "Спеціалізація(ШІ):\n" + result_text_specialization_output.toPlainText() + "\n\n"
                            "Спеціалізація(Алгоритмічна):\n" + result_text_algorhythm_specialization_output.toPlainText() + "\n\n"
                            "Тон тексту:\n" + result_text_tone_output.toPlainText() + "\n\n"
                            "Найголовніші речення:\n" + result_main_sentence_output.toPlainText() + "\n\n"
                            "Статистика тексту:\n" + statistics_text + "\n"
                            f"Графік Zipf доступний у файлі {zipf_image_path} у тій самій директорії."
                        )
                    QMessageBox.information(text_input, "Збережено", "Результати успішно збережено у файл.")
            except Exception as e:
                QMessageBox.critical(text_input, "Помилка", f"Помилка при збереженні файлу: {str(e)}")