from PyQt6.QtWidgets import QWidget, QVBoxLayout, QApplication
from PyQt6.QtCore import Qt
from AlgorhythmBasedTextAnalysis.TextStatistics import TextStatistics
from UI.UiComponents import UIComponents
from UI.AnalysisLogic import AnalysisLogic

class AnalysisWidget(QWidget):
    """Головний віджет, що містить графічний інтерфейс програми."""

    def __init__(self, model):
        super().__init__()
        self.model = model
        self.text_stats = TextStatistics()
        self.initUI()

    def initUI(self):
        """Налаштовує графічний інтерфейс."""

        self.setWindowTitle("Інтелектуальний аналіз текстів")

        # Отримуємо розміри екрану
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()

        # Встановлюємо розміри вікна залежно від розміру екрана (наприклад, 70% x 85%)
        window_width = int(screen_width * 0.7)
        window_height = int(screen_height * 0.85)
        self.setGeometry(
            (screen_width - window_width) // 2,
            (screen_height - window_height) // 2,
            window_width,
            window_height
        )

        # Оформлення
        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(15)
        self.layout.setContentsMargins(20, 20, 20, 20)

        self.setStyleSheet("""
            QWidget {
                font-family: Arial;
                font-size: 14px;
                background-color: #f5f6fa;
            }
        """)

        # Створюємо UI-компоненти
        self.text_input = UIComponents.create_input_section(self.layout)
        self.analyze_button = UIComponents.create_button_section(
            self.layout, self.load_file, self.start_analysis, self.save_results
        )
        outputs = UIComponents.create_result_section(self.layout)

        # Ініціалізуємо логіку
        self.logic = AnalysisLogic(self.model, self.text_stats, self.text_input, self.analyze_button, outputs)

    def load_file(self):
        self.logic.load_file()

    def start_analysis(self):
        self.logic.start_analysis()

    def update_result(self, main_sentences, specialization):
        self.logic.update_result(main_sentences, specialization)

    def save_results(self):
        self.logic.save_results()
