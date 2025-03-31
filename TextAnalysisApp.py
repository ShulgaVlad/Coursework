from PyQt6.QtWidgets import QApplication
from AIApiConnect.AIModel import AIModel
from AnalysisWidget import AnalysisWidget

class TextAnalysisApp(QApplication):
    """Головний клас програми."""

    def __init__(self, sys_argv):
        super().__init__(sys_argv)
        self.model = AIModel()
        self.window = AnalysisWidget(self.model)
        self.window.show()
