from PyQt6.QtGui import QPixmap
from scipy.stats import linregress
import matplotlib.pyplot as plt
import math
import numpy as np

class ZipfAnalyze:
    def __init__(self):
        self.statistics_text = ""
        self.zipf_image_path = None
        self.s_value = None

    def calculate_s_value(self, frequencies):
        freqs = [freq for _, freq in frequencies if freq >= 1]
        if len(freqs) < 2:
            return 0

        ranks = np.arange(1, len(freqs) + 1)
        log_ranks = np.log(ranks)
        log_freqs = np.log(freqs)

        slope, intercept, r_value, p_value, std_err = linregress(log_ranks, log_freqs)
        self.s_value = -slope
        return round(self.s_value, 3)

    def plot_zipf_law(self, frequencies, save_path="zipf_plot.png"):
        freqs = [freq for _, freq in frequencies if freq >= 1]
        if not freqs:
            print("Немає даних для побудови графіка.")
            return None

        ranks = list(range(1, len(freqs) + 1))
        log_ranks = [np.log(r) for r in ranks]
        log_freqs = [np.log(f) for f in freqs]

        # Обчислення коефіцієнта
        self.calculate_s_value(frequencies)

        # Побудова графіка
        plt.figure(figsize=(8, 6))
        plt.plot(log_ranks, log_freqs, marker='o', linestyle='-', color='blue')
        plt.title("Закон Зіпфа (log(rank) vs log(frequency))")
        plt.xlabel("log(Ранг)")
        plt.ylabel("log(Частота)")
        plt.grid(True)

        if self.s_value is not None:
            plt.figtext(0.5, 0.01,
                        f"Коефіцієнт s (нахил кривої): {round(self.s_value, 3)}",
                        ha="center", fontsize=10, color='black')

        plt.tight_layout(rect=[0, 0.03, 1, 1])  # залишаємо місце для підпису
        plt.savefig(save_path)
        plt.close()

        self.zipf_image_path = save_path
        return QPixmap(save_path)
