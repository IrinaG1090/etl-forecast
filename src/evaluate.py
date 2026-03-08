import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
import config as cfg

def load_results():
    pred_path = cfg.DATA_DIR / "predictions.csv"
    df = pd.read_csv(pred_path, parse_dates=['timestamp'])
    return df

def plot_predictions(df):
    plt.figure(figsize=(14, 6))
    plt.plot(df['timestamp'], df['actual'], label='Фактические', color='blue', alpha=0.7)
    plt.plot(df['timestamp'], df['predicted'], label='Предсказанные', color='red', alpha=0.7, linestyle='--')
    plt.title('Прогнозирование временного ряда')
    plt.xlabel('Дата')
    plt.ylabel('Значение')
    plt.legend()
    plt.grid(True, alpha=0.3)
    output_path = cfg.REPORTS_DIR / "predictions_plot.png"
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.show()
    print(f"[OK] График сохранён: {output_path}")

def plot_residuals(df):
    df['residual'] = df['actual'] - df['predicted']
    plt.figure(figsize=(14, 5))
    plt.subplot(1, 2, 1)
    plt.plot(df['timestamp'], df['residual'], color='green', alpha=0.7)
    plt.axhline(y=0, color='red', linestyle='--', alpha=0.5)
    plt.title('Остатки модели')
    plt.xlabel('Дата')
    plt.ylabel('Остаток')
    plt.grid(True, alpha=0.3)
    plt.subplot(1, 2, 2)
    plt.hist(df['residual'], bins=30, color='green', alpha=0.7, edgecolor='black')
    plt.title('Распределение остатков')
    plt.xlabel('Остаток')
    plt.ylabel('Частота')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    output_path = cfg.REPORTS_DIR / "residuals_plot.png"
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.show()
    print(f"[OK] График остатков сохранён: {output_path}")

if __name__ == "__main__":
    df = load_results()
    plot_predictions(df)
    plot_residuals(df)