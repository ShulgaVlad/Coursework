from PyQt6.QtCore import QThread, pyqtSignal
import re

class AnalysisThread(QThread):
    """Потік для асинхронного аналізу тексту, щоб уникнути зависання UI."""
    result_signal = pyqtSignal(str, str)

    def __init__(self, model, text):
        super().__init__()
        self.model = model
        self.text = text

    def run(self):
        """Запускає аналіз тексту в окремому потоці."""
        prompt_main = f'Надай лише найголовніші речення серед тексту, за якими можна зрозуміти сенс тексту, повністю цитуючи та не змінюючи їх. Якщо найголовніші речення не визначені за якихось причин, надай відповідь "Не визначено": {self.text}'
        prompt_specialization = f'Надай лише його спеціалізацію. Якщо спеціалізація не визначена за якихось причин, надай відповідь "Не визначено": {self.text}'

        main_sentences = self.model.generate_response(prompt_main)
        sentences = re.split(r'(?<=[.!?])\s+', main_sentences)
        cleaned_sentences = [re.sub(r'\s+', ' ', s.strip()) for s in sentences if s.strip()]
        main_sentences = ' '.join(cleaned_sentences)
        specialization = self.model.generate_response(prompt_specialization)

        self.result_signal.emit(main_sentences.strip(), specialization.strip())