from PyQt6.QtWidgets import (QTextEdit, QPushButton, QLabel, QHBoxLayout, QGroupBox, QApplication, QDialog, QVBoxLayout)
from PyQt6.QtCore import Qt

class TextEditDialog(QDialog):
    """Модальне вікно для відображення розширеного QTextEdit."""
    def __init__(self, text, title, parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setModal(True)
        if title == "Введення тексту":
            # Отримуємо розміри екрану
            screen = QApplication.primaryScreen()
            screen_geometry = screen.availableGeometry()
            screen_width = screen_geometry.width()
            screen_height = screen_geometry.height()

            # Встановлюємо розміри вікна залежно від розміру екрана (наприклад, 70% x 85%)
            window_width = int(screen_width * 0.65)
            window_height = int(screen_height * 0.85)
            self.setGeometry(
                (screen_width - window_width) // 2,
                (screen_height - window_height) // 2,
                window_width,
                window_height
            )
        else:
            self.resize(600, 400)

        layout = QVBoxLayout()
        text_edit = QTextEdit()
        text_edit.setReadOnly(False)
        text_edit.setText(text)
        text_edit.setStyleSheet("""
            QTextEdit {
                border: 1px solid #dfe4ea;
                border-radius: 8px;
                padding: 10px;
                background-color: #ffffff;
                color: black;
            }
        """)
        layout.addWidget(text_edit)

        close_button = QPushButton("Закрити")
        close_button.setStyleSheet("""
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
        close_button.clicked.connect(self.accept)
        layout.addWidget(close_button)

        self.setLayout(layout)

class UIComponents:
    @staticmethod
    def create_input_section(layout):
        """Створює секцію для введення тексту."""
        label = QLabel("Введіть текст для аналізу:")
        label.setStyleSheet("font-weight: bold; color: #2f3542;")

        # Контейнер для QTextEdit і кнопки
        input_container = QHBoxLayout()

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
        text_input.setFixedHeight(100)  # Початкова висота

        # Кнопка для відкриття модального вікна
        toggle_button = QPushButton("↕")
        toggle_button.setFixedWidth(30)
        toggle_button.setStyleSheet("""
                QPushButton {
                    background-color: #dfe4ea;
                    border-radius: 4px;
                    padding: 5px;
                }
                QPushButton:hover {
                    background-color: #ced4da;
                }
                QPushButton:pressed {
                    background-color: #adb5bd;
                }
            """)

        def open_dialog():
            dialog = TextEditDialog(text_input.toPlainText(), "Введення тексту", text_input)
            dialog.exec()

        toggle_button.clicked.connect(open_dialog)

        input_container.addWidget(text_input)
        input_container.addWidget(toggle_button)
        input_container.setAlignment(toggle_button, Qt.AlignmentFlag.AlignTop)

        layout.addWidget(label)
        layout.addLayout(input_container)
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

        # Функція для створення QTextEdit з кнопкою для модального вікна
        def create_text_edit_with_dialog(default_height, style, title):
            container = QHBoxLayout()
            text_edit = QTextEdit()
            text_edit.setReadOnly(True)
            text_edit.setFixedHeight(default_height)
            text_edit.setStyleSheet(style)

            toggle_button = QPushButton("↕")
            toggle_button.setFixedWidth(30)
            toggle_button.setStyleSheet("""
                QPushButton {
                    background-color: #dfe4ea;
                    border-radius: 4px;
                    padding: 5px;
                }
                QPushButton:hover {
                    background-color: #ced4da;
                }
                QPushButton:pressed {
                    background-color: #adb5bd;
                }
            """)

            def open_dialog():
                dialog = TextEditDialog(text_edit.toPlainText(), title, result_group)
                dialog.exec()

            toggle_button.clicked.connect(open_dialog)
            container.addWidget(text_edit)
            container.addWidget(toggle_button)
            container.setAlignment(toggle_button, Qt.AlignmentFlag.AlignTop)
            return container, text_edit

        # Спеціалізація(ШІ)
        result_text_specialization_label = QLabel("Спеціалізація(ШІ):")
        result_text_specialization_label.setStyleSheet("font-weight: bold; color: #2f3542; padding-left: 5px; margin-top: 15px;")
        result_text_specialization_label.setFixedHeight(40)

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

        # Спеціалізація(Алгоритмічна)
        result_text_algorhythm_specialization_label = QLabel("Спеціалізація(Алгоритмічна):")
        result_text_algorhythm_specialization_label.setStyleSheet("font-weight: bold; color: #2f3542; padding-left: 5px;")
        result_text_algorhythm_specialization_label.setFixedHeight(25)

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

        # Тон тексту
        result_text_tone_label = QLabel("Тон тексту:")
        result_text_tone_label.setStyleSheet("font-weight: bold; color: #2f3542; padding-left: 5px;")
        result_text_tone_label.setFixedHeight(25)

        result_text_tone_output = QTextEdit()
        result_text_tone_output.setReadOnly(True)
        result_text_tone_output.setFixedHeight(40)
        result_text_tone_output.setStyleSheet("""
            QTextEdit {
                border: 1px solid #dfe4ea;
                border-radius: 8px;
                padding: 5px;
                background-color: #ffffff;
                color: black;
            }
        """)

        # Найголовніші речення
        result_main_sentence_label = QLabel("Найголовніші речення:")
        result_main_sentence_label.setStyleSheet("font-weight: bold; color: #2f3542; padding-left: 5px;")
        result_main_sentence_label.setFixedHeight(25)

        main_sentence_style = """
            QTextEdit {
                border: 1px solid #dfe4ea;
                border-radius: 8px;
                padding: 10px;
                background-color: #ffffff;
                color: black;
            }
        """
        main_sentence_container, result_main_sentence_output = create_text_edit_with_dialog(100, main_sentence_style, "Найголовніші речення")

        # Статистика тексту
        result_text_statistics_label = QLabel("Статистика тексту:")
        result_text_statistics_label.setStyleSheet("font-weight: bold; color: #2f3542; padding-left: 5px;")
        result_text_statistics_label.setFixedHeight(25)

        statistics_container, result_text_statistics_output = create_text_edit_with_dialog(100, main_sentence_style, "Статистика тексту")

        # Закон Зіпфа
        zipf_label = QLabel("Закон Зіпфа:")
        zipf_label.setStyleSheet("font-weight: bold; color: #2f3542; padding-left: 5px;")
        zipf_label.setFixedHeight(25)

        result_zipf_image = QLabel()
        result_zipf_image.setMinimumSize(600, 400)
        result_zipf_image.setAlignment(Qt.AlignmentFlag.AlignCenter)
        result_zipf_image.setStyleSheet("""
            QLabel {
                border: 1px solid #dfe4ea;
                border-radius: 8px;
                background-color: #ffffff;
            }
        """)

        # Ліва колонка (всі текстові поля)
        left_layout = QVBoxLayout()
        left_layout.setSpacing(10)

        left_layout.addWidget(result_text_specialization_label)
        left_layout.addWidget(result_text_specialization_output)

        left_layout.addWidget(result_text_algorhythm_specialization_label)
        left_layout.addWidget(result_text_algorhythm_specialization_output)

        left_layout.addWidget(result_text_tone_label)
        left_layout.addWidget(result_text_tone_output)

        left_layout.addWidget(result_main_sentence_label)
        left_layout.addLayout(main_sentence_container)

        left_layout.addWidget(result_text_statistics_label)
        left_layout.addLayout(statistics_container)

        # Права колонка (тільки графік)
        right_layout = QVBoxLayout()
        right_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        right_layout.addWidget(zipf_label)
        right_layout.addWidget(result_zipf_image)

        # Основний макет — горизонтально
        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout, stretch=2)
        main_layout.addLayout(right_layout, stretch=1)

        result_group.setLayout(main_layout)
        layout.addWidget(result_group)

        return (result_text_specialization_output, result_text_algorhythm_specialization_output,
                result_main_sentence_output, result_text_statistics_output, result_text_tone_output,
                result_zipf_image)