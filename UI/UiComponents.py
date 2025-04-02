from PyQt6.QtWidgets import (QTextEdit, QPushButton, QLabel, QHBoxLayout, QGroupBox, QVBoxLayout)
from PyQt6.QtCore import Qt

class UIComponents:
    @staticmethod
    def create_input_section(layout):
        """Створює секцію для введення тексту."""
        label = QLabel("Введіть текст для аналізу:")
        label.setStyleSheet("font-weight: bold; color: #2f3542;")

        text_input = QTextEdit()
        text_input.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        text_input.setStyleSheet("""
            QTextEdit {
                border: 1px solid #dfe4ea;
                border-radius: 8px;
                padding: 10px;
                background-color: #ffffff;
                color: black;
            }
        """)

        layout.addWidget(label)
        layout.addWidget(text_input)
        return text_input

    @staticmethod
    def create_button_section(layout, load_file_callback, start_analysis_callback, save_results_callback):
        """Створює секцію з кнопками."""
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)

        file_button = QPushButton("Відкрити файл")
        file_button.clicked.connect(load_file_callback)
        file_button.setStyleSheet("""
            QPushButton {
                background-color: #4dabf7;
                color: white;
                border-radius: 8px;
                padding: 8px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #339af0;
            }
            QPushButton:pressed {
                background-color: #228be6;
            }
        """)
        button_layout.addWidget(file_button)

        analyze_button = QPushButton("Аналізувати")
        analyze_button.clicked.connect(start_analysis_callback)
        analyze_button.setStyleSheet("""
            QPushButton {
                background-color: #40c057;
                color: white;
                border-radius: 8px;
                padding: 8px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #37b24d;
            }
            QPushButton:pressed {
                background-color: #2f9e44;
            }
            QPushButton:disabled {
                background-color: #adb5bd;
            }
        """)
        button_layout.addWidget(analyze_button)

        save_button = QPushButton("Зберегти результат")
        save_button.clicked.connect(save_results_callback)
        save_button.setStyleSheet("""
            QPushButton {
                background-color: #ff922b;
                color: white;
                border-radius: 8px;
                padding: 8px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #f76707;
            }
            QPushButton:pressed {
                background-color: #e8590c;
            }
        """)
        button_layout.addWidget(save_button)

        layout.addLayout(button_layout)
        return analyze_button

    @staticmethod
    def create_result_section(layout):
        """Створює секцію для результатів."""
        result_group = QGroupBox("Результати аналізу")
        result_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                color: #2f3542;
                border: 1px solid #dfe4ea;
                border-radius: 8px;
                padding: 10px;
                background-color: #ffffff;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top left;
                padding-top: 10px; 
                padding-left: 10px;
                background-color: transparent;
            }
        """)
        result_layout = QVBoxLayout()
        result_layout.setSpacing(10)

        # Спеціалізація(ШІ)
        result_text_specialization_label = QLabel("Спеціалізація(ШІ):")
        result_text_specialization_label.setStyleSheet("font-weight: bold; color: #2f3542; border-radius: 5px; padding-left: 5px; margin-top: 15px;")
        result_text_specialization_label.setFixedHeight(40)
        result_layout.addWidget(result_text_specialization_label)

        result_text_specialization_output = QTextEdit()
        result_text_specialization_output.setReadOnly(True)
        result_text_specialization_output.setFixedHeight(40)
        result_text_specialization_output.setStyleSheet("""
            QTextEdit {
                border: 1px solid #dfe4ea;
                border-radius: 8px;
                padding: 5px;
                background-color: #ffffff;
                color: black;
            }
        """)
        result_layout.addWidget(result_text_specialization_output)

        # Спеціалізація(Алгоритмічна)
        result_text_algorhythm_specialization_label = QLabel("Спеціалізація(Алгоритмічна):")
        result_text_algorhythm_specialization_label.setStyleSheet("font-weight: bold; color: #2f3542; border-radius: 5px; padding-left: 5px;")
        result_text_algorhythm_specialization_label.setFixedHeight(25)
        result_layout.addWidget(result_text_algorhythm_specialization_label)

        result_text_algorhythm_specialization_output = QTextEdit()
        result_text_algorhythm_specialization_output.setReadOnly(True)
        result_text_algorhythm_specialization_output.setFixedHeight(40)
        result_text_algorhythm_specialization_output.setStyleSheet("""
            QTextEdit {
                border: 1px solid #dfe4ea;
                border-radius: 8px;
                padding: 5px;
                background-color: #ffffff;
                color: black;
            }
        """)
        result_layout.addWidget(result_text_algorhythm_specialization_output)

        # Найголовніші речення
        result_main_sentence_label = QLabel("Найголовніші речення:")
        result_main_sentence_label.setStyleSheet("font-weight: bold; color: #2f3542; border-radius: 5px; padding-left: 5px;")
        result_main_sentence_label.setFixedHeight(25)
        result_layout.addWidget(result_main_sentence_label)

        result_main_sentence_output = QTextEdit()
        result_main_sentence_output.setReadOnly(True)
        result_main_sentence_output.setStyleSheet("""
            QTextEdit {
                border: 1px solid #dfe4ea;
                border-radius: 8px;
                padding: 10px;
                background-color: #ffffff;
                color: black;
            }
        """)
        result_layout.addWidget(result_main_sentence_output)

        # Статистика тексту
        result_text_statistics_label = QLabel("Статистика тексту:")
        result_text_statistics_label.setStyleSheet("font-weight: bold; color: #2f3542; border-radius: 5px; padding-left: 5px;")
        result_text_statistics_label.setFixedHeight(25)
        result_layout.addWidget(result_text_statistics_label)

        result_text_statistics_output = QTextEdit()
        result_text_statistics_output.setReadOnly(True)
        result_text_statistics_output.setFixedHeight(100)
        result_text_statistics_output.setStyleSheet("""
            QTextEdit {
                border: 1px solid #dfe4ea;
                border-radius: 8px;
                padding: 5px;
                background-color: #ffffff;
                color: black;
            }
        """)
        result_layout.addWidget(result_text_statistics_output)

        result_group.setLayout(result_layout)
        layout.addWidget(result_group)

        return (result_text_specialization_output, result_text_algorhythm_specialization_output,
                result_main_sentence_output, result_text_statistics_output)