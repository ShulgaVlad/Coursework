import sys
from PyQt6.QtWidgets import QApplication
from UI.MainWidget import AnalysisWidget
from AIApiConnect.AIModel import AIModel  # Замініть на ваш модуль

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setStyleSheet("""
            QMessageBox QLabel {                 
                color: black;                 
            } 
            QMessageBox QPushButton { 
                color: black; 
            }
        """)

    # Ініціалізуємо модель
    model = AIModel()  # Замініть на реальну ініціалізацію вашої моделі
    window = AnalysisWidget(model=model)  # Передаємо ініціалізовану модель
    window.show()
    sys.exit(app.exec())