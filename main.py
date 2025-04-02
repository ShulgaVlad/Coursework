import sys
import time
from PyQt6.QtWidgets import QApplication, QSplashScreen, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt, QTimer, QEvent
from PyQt6.QtGui import QPixmap, QPainter, QColor, QFont
from UI.MainWidget import AnalysisWidget
from AIApiConnect.AIModel import AIModel  # Замініть на ваш модуль


# class SplashScreen(QSplashScreen):
#     def __init__(self):
#         super().__init__(QPixmap("splash.png"))  # Замініть на ваш шлях до зображення
#         self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
#         self.setStyleSheet("background-color: #2c3e50; border: 2px solid #ecf0f1; width: 100px; height: 500px;")
#
#         # Додаємо кастомний лейаут для тексту
#         self.label = QLabel("Завантаження...", self)
#         self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
#         self.label.setStyleSheet("color: white; font-size: 18px;")
#
#         layout = QVBoxLayout(self)
#         layout.addWidget(self.label)
#
#         self.drag_position = None
#         self.installEventFilter(self)
#
#     def eventFilter(self, obj, event):
#         if event.type() == QEvent.Type.MouseButtonPress and event.button() == Qt.MouseButton.LeftButton:
#             self.drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
#             event.accept()
#             return True
#         elif event.type() == QEvent.Type.MouseMove and self.drag_position is not None:
#             self.move(event.globalPosition().toPoint() - self.drag_position)
#             event.accept()
#             return True
#         elif event.type() == QEvent.Type.MouseButtonRelease:
#             self.drag_position = None
#             event.accept()
#             return True
#         return super().eventFilter(obj, event)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     app.setStyle("Fusion")
#     app.setStyleSheet("""
#             QMessageBox QLabel {
#                 color: black;
#             }
#             QMessageBox QPushButton {
#                 color: black;
#             }
#         """)
#
#     # Створюємо сплеш-скрін
#     splash = SplashScreen()
#     splash.show()
#
#     # Затримка у 3 секунди перед відкриттям головного вікна
#     QTimer.singleShot(3000, splash.close)
#
#     # Ініціалізуємо модель після закриття сплеш-скріну
#     model = AIModel()  # Замініть на реальну ініціалізацію вашої моделі
#     window = AnalysisWidget(model=model)
#     QTimer.singleShot(3000, window.show)
#
#     sys.exit(app.exec())

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
    window.move(500, 50)
    window.show()
    sys.exit(app.exec())