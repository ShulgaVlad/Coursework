from PyQt6.QtGui import QPixmap
import matplotlib.pyplot as plt
import math

class ZipfAnalyze:
    def __init__(self):
        self.statistics_text = ""
        self.zipf_image_path = None

    def plot_zipf_law(self, frequencies, save_path="zipf_plot.png"):
        freqs = [freq for _, freq in frequencies]
        if not freqs:
            print("Немає даних для побудови графіка.")
            return None

        ranks = list(range(1, len(freqs) + 1))
        log_ranks = [math.log(r) for r in ranks]
        log_freqs = [math.log(f) for f in freqs]

        plt.figure(figsize=(8, 6))
        plt.plot(log_ranks, log_freqs, marker='o', linestyle='-', color='blue')
        plt.title("Закон Зіпфа (log(rank) vs log(frequency))")
        plt.xlabel("log(Ранг)")
        plt.ylabel("log(Частота)")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()

        self.zipf_image_path = save_path
        return QPixmap(save_path)
