import numpy as np
import pandas as pd
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
import config as cfg

def generate_time_series(
    n_points=cfg.N_POINTS,
    trend_strength=cfg.TREND_STRENGTH,
    seasonality_period=cfg.SEASONALITY_PERIOD,
    noise_level=cfg.NOISE_LEVEL,
    random_seed=cfg.RANDOM_SEED
):
    np.random.seed(random_seed)
    timestamps = pd.date_range(start='2020-01-01', periods=n_points, freq='D')
    t = np.arange(n_points)
    trend = trend_strength * t
    seasonality = np.sin(2 * np.pi * t / seasonality_period)
    noise = np.random.normal(0, noise_level, n_points)
    values = 100 + trend + 10 * seasonality + noise
    values += 0.001 * (t - n_points/2) ** 2
    values += 2 * np.sin(2 * np.pi * t / 7)
    df = pd.DataFrame({'timestamp': timestamps, 'value': values})
    return df

def save_raw_data(df):
    output_path = cfg.DATA_DIR / "raw_data.csv"
    df.to_csv(output_path, index=False)
    print(f"[OK] Сырые данные сохранены: {output_path}")
    return df

if __name__ == "__main__":
    df = generate_time_series()
    save_raw_data(df)