import sys
import time
from PyQt6.QtWidgets import QApplication, QSplashScreen, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt, QTimer, QEvent
from PyQt6.QtGui import QPixmap, QPainter, QColor, QFont
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