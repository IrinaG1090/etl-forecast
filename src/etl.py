import pandas as pd
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
import config as cfg

def load_raw_data():
    file_path = cfg.DATA_DIR / "raw_data.csv"
    if not file_path.exists():
        raise FileNotFoundError(f"Файл {file_path} не найден. Сначала запусти generate_data.py")
    df = pd.read_csv(file_path, parse_dates=['timestamp'])
    return df

def clean_data(df):
    if df['value'].isnull().any():
        df['value'] = df['value'].interpolate(method='linear')
    df = df.sort_values('timestamp').reset_index(drop=True)
    return df

def save_cleaned_data(df):
    output_path = cfg.DATA_DIR / "cleaned_data.csv"
    df.to_csv(output_path, index=False)
    print(f"[OK] Очищенные данные сохранены: {output_path}")
    return df

if __name__ == "__main__":
    df = load_raw_data()
    df_clean = clean_data(df)
    save_cleaned_data(df_clean)