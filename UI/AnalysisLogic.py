from AITextAnalysis.AnalysisThread import AnalysisThread
from AlgorhythmBasedTextAnalysis.AlgorhythmTextAnalysis import AlgorhythmTextAnalysis
from FileControl.ReadTxtFile import FileLoader
from AITextAnalysis.TextHighlighter import TextHighlighter
from AlgorhythmBasedTextAnalysis.LexicalSentimentAnalysis.LexicalSentimentAnalysis import LexicalSentimentAnalysis
from AlgorhythmBasedTextAnalysis.ZipfAnalyze import ZipfAnalyze


class AnalysisLogic:
    def __init__(self, model, text_stats, text_input, analyze_button, outputs, widget):
        self.model = model
        self.text_stats = text_stats
        self.text_input = text_input
        self.analyze_button = analyze_button

        # Розпаковуємо повернені віджети
        (self.result_text_specialization_output,
         self.result_text_algorhythm_specialization_output,
         self.result_main_sentence_output,
         self.result_text_statistics_output,
         self.result_text_tone_output,
         self.result_zipf_image) = outputs

        # Зберігаємо посилання на головний віджет для масштабування зображення
        self.widget = widget

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
        text = self.text_input.toPlainText()
        lemmas, top_words = self.text_stats.calculate_text_statistics(text)

        # Алгоритмічний аналіз
        analyzer = AlgorhythmTextAnalysis(top_words)
        detected_specialization = analyzer.run()

        # Аналіз тону
        tone = LexicalSentimentAnalysis.lexical_sentiment_analysis(lemmas)

        # Закон Зіпфа
        zipf_analyzer = ZipfAnalyze()
        zipf_pixmap = zipf_analyzer.plot_zipf_law(top_words)

        self.result_main_sentence_output.setText(main_sentences)
        self.result_text_specialization_output.setText(specialization)
        self.result_text_statistics_output.setText(self.text_stats.statistics_text)
        self.result_text_algorhythm_specialization_output.setText(detected_specialization)
        self.result_text_tone_output.setText(tone)

        # Відображення графіка
        if zipf_pixmap:
            self.result_zipf_image.setPixmap(zipf_pixmap.scaledToWidth(600))

        TextHighlighter.highlight_text(self.text_input, text, main_sentences)
        self.analyze_button.setEnabled(True)