from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton, QLabel, QFileDialog, QMessageBox
from PyQt6.QtCore import Qt
from AITextAnalysis.AnalysisThread import AnalysisThread
from AlgorhythmBasedTextAnalysis.AlgorhythmTextAnalysis import AlgorhythmTextAnalysis
from ReadTxtFile import FileLoader
from AITextAnalysis.TextHighlighter import TextHighlighter
from AlgorhythmBasedTextAnalysis.TextStatistics import TextStatistics

class AnalysisWidget(QWidget):
    """Головний віджет, що містить графічний інтерфейс програми."""

    def __init__(self, model):
        super().__init__()
        self.model = model
        self.text_stats = TextStatistics()  # Створюємо інстанс TextStatistics
        self.initUI()

    def initUI(self):
        """Налаштовує графічний інтерфейс."""
        self.setWindowTitle("Інтелектуальний аналіз текстів")
        self.setGeometry(100, 100, 600, 500)

        self.layout = QVBoxLayout(self)

        self.label = QLabel("Введіть текст для аналізу:")
        self.layout.addWidget(self.label)

        self.file_button = QPushButton("Відкрити файл")
        self.file_button.clicked.connect(self.load_file)
        self.layout.addWidget(self.file_button)

        self.text_input = QTextEdit()
        self.text_input.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.layout.addWidget(self.text_input)

        self.analyze_button = QPushButton("Аналізувати")
        self.analyze_button.clicked.connect(self.start_analysis)
        self.layout.addWidget(self.analyze_button)

        self.result_main_sentence_label = QLabel("Найголовніші речення:")
        self.layout.addWidget(self.result_main_sentence_label)

        self.result_main_sentence_output = QTextEdit()
        self.result_main_sentence_output.setReadOnly(True)
        self.layout.addWidget(self.result_main_sentence_output)

        self.result_text_specialization_label = QLabel("Спеціалізація(ШІ):")
        self.layout.addWidget(self.result_text_specialization_label)

        self.result_text_specialization_output = QTextEdit()
        self.result_text_specialization_output.setReadOnly(True)
        self.result_text_specialization_output.setFixedHeight(30)
        self.layout.addWidget(self.result_text_specialization_output)

        self.result_text_statistics_label = QLabel("Статистика тексту:")
        self.layout.addWidget(self.result_text_statistics_label)

        self.result_text_statistics_output = QTextEdit()
        self.result_text_statistics_output.setReadOnly(True)
        self.result_text_statistics_output.setFixedHeight(100)
        self.layout.addWidget(self.result_text_statistics_output)

        self.result_text_algorhythm_specialization_label = QLabel("Спеціалізація(Алгоритмічна):")
        self.layout.addWidget(self.result_text_algorhythm_specialization_label)

        self.result_text_algorhythm_specialization_output = QTextEdit()
        self.result_text_algorhythm_specialization_output.setReadOnly(True)
        self.result_text_algorhythm_specialization_output.setFixedHeight(30)
        self.layout.addWidget(self.result_text_algorhythm_specialization_output)

        self.save_button = QPushButton("Зберегти результат")
        self.save_button.clicked.connect(self.save_results)
        self.layout.addWidget(self.save_button)

    def load_file(self):
        """Завантажує текст з файлу у поле введення."""
        text = FileLoader.load_text_from_file(self)
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
        top_words = self.text_stats.calculate_text_statistics(text)  # Викликаємо через інстанс
        analyzer = AlgorhythmTextAnalysis(top_words)
        detected_specialization = analyzer.run()

        self.result_main_sentence_output.setText(main_sentences)
        self.result_text_specialization_output.setText(specialization)
        self.result_text_statistics_output.setText(self.text_stats.statistics_text)  # Використовуємо статистику з TextStatistics
        TextHighlighter.highlight_text(self.text_input, text, main_sentences)
        self.result_text_algorhythm_specialization_output.setText(detected_specialization)
        self.analyze_button.setEnabled(True)

    def save_results(self):
        """Зберігає результати аналізу у текстовий файл."""
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(self, "Зберегти результат", "", "Text Files (*.txt)")

        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write("Результати аналізу тексту:\n\n")
                    file.write("Найголовніші речення:\n")
                    file.write(self.result_main_sentence_output.toPlainText() + "\n\n")
                    file.write("Спеціалізація(ШІ):\n")
                    file.write(self.result_text_specialization_output.toPlainText() + "\n\n")
                    file.write("Спеціалізація(Алгоритмічна):\n")
                    file.write(self.result_text_algorhythm_specialization_output.toPlainText() + "\n\n")
                    file.write("Статистика тексту:\n")
                    file.write(self.text_stats.statistics_text + "\n")  # Використовуємо статистику з TextStatistics

                QMessageBox.information(self, "Збережено", "Результати успішно збережено у файл.")
            except Exception as e:
                QMessageBox.critical(self, "Помилка", f"Помилка при збереженні файлу: {str(e)}")