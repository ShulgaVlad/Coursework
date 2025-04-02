from PyQt6.QtWidgets import QFileDialog, QMessageBox
from AITextAnalysis.AnalysisThread import AnalysisThread
from AlgorhythmBasedTextAnalysis.AlgorhythmTextAnalysis import AlgorhythmTextAnalysis
from ReadTxtFile import FileLoader
from AITextAnalysis.TextHighlighter import TextHighlighter

class AnalysisLogic:
    def __init__(self, model, text_stats, text_input, analyze_button, outputs):
        self.model = model
        self.text_stats = text_stats
        self.text_input = text_input
        self.analyze_button = analyze_button
        self.result_text_specialization_output, self.result_text_algorhythm_specialization_output, \
            self.result_main_sentence_output, self.result_text_statistics_output = outputs

    def load_file(self):
        """Завантажує текст з файлу у поле введення."""
        text = FileLoader.load_text_from_file(self.text_input)
        if text:
            self.text_input.setText(text)

    def start_analysis(self):
        """Запускає потік аналізу тексту."""
        text = self.text_input.toPlainText().strip()
        if text:
            self.analyze_button.setEnabled(False)
            self.analysis_thread = AnalysisThread(self.model, text)
            self.analysis_thread.result_signal.connect(self.update_result)
            self.analysis_thread.start()

    def update_result(self, main_sentences, specialization):
        """Оновлює UI з отриманими результатами."""
        text = self.text_input.toPlainText()
        top_words = self.text_stats.calculate_text_statistics(text)
        analyzer = AlgorhythmTextAnalysis(top_words)
        detected_specialization = analyzer.run()

        self.result_main_sentence_output.setText(main_sentences)
        self.result_text_specialization_output.setText(specialization)
        self.result_text_statistics_output.setText(self.text_stats.statistics_text)
        TextHighlighter.highlight_text(self.text_input, text, main_sentences)
        self.result_text_algorhythm_specialization_output.setText(detected_specialization)
        self.analyze_button.setEnabled(True)

    def save_results(self):
        """Зберігає результати аналізу у текстовий файл."""
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(self.text_input, "Зберегти результат", "", "Text Files (*.txt)")
        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write("Результати аналізу тексту:\n\n")
                    file.write("Спеціалізація(ШІ):\n")
                    file.write(self.result_text_specialization_output.toPlainText() + "\n\n")
                    file.write("Спеціалізація(Алгоритмічна):\n")
                    file.write(self.result_text_algorhythm_specialization_output.toPlainText() + "\n\n")
                    file.write("Найголовніші речення:\n")
                    file.write(self.result_main_sentence_output.toPlainText() + "\n\n")
                    file.write("Статистика тексту:\n")
                    file.write(self.text_stats.statistics_text + "\n")
                QMessageBox.information(self.text_input, "Збережено", "Результати успішно збережено у файл.")
            except Exception as e:
                QMessageBox.critical(self.text_input, "Помилка", f"Помилка при збереженні файлу: {str(e)}")
