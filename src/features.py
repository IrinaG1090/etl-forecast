import pandas as pd
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
import config as cfg

def create_lag_features(df, column='value', lags=cfg.N_LAGS):
    df_feat = df.copy()
    for lag in range(1, lags + 1):
        df_feat[f'lag_{lag}'] = df_feat[column].shift(lag)
    return df_feat

def create_rolling_features(df, column='value', windows=[7, 14, 30]):
    df_feat = df.copy()
    for window in windows:
        df_feat[f'rolling_mean_{window}'] = df_feat[column].rolling(window=window).mean()
        df_feat[f'rolling_std_{window}'] = df_feat[column].rolling(window=window).std()
    return df_feat

def create_date_features(df):
    df_feat = df.copy()
    df_feat['dayofweek'] = df_feat['timestamp'].dt.dayofweek
    df_feat['month'] = df_feat['timestamp'].dt.month
    df_feat['day'] = df_feat['timestamp'].dt.day
    df_feat['quarter'] = df_feat['timestamp'].dt.quarter
    df_feat['dayofyear'] = df_feat['timestamp'].dt.dayofyear
    df_feat['weekend'] = (df_feat['dayofweek'] >= 5).astype(int)
    return df_feat

def create_features_pipeline(df):
    df_feat = create_date_features(df)
    df_feat = create_lag_features(df_feat)
    df_feat = create_rolling_features(df_feat)
    df_feat = df_feat.dropna().reset_index(drop=True)
    return df_feat

def save_features(df):
    output_path = cfg.DATA_DIR / "features_data.csv"
    df.to_csv(output_path, index=False)
    print(f"[OK] Данные с признаками сохранены: {output_path}")
    return df

if __name__ == "__main__":
    df = pd.read_csv(cfg.DATA_DIR / "cleaned_data.csv", parse_dates=['timestamp'])
    df_feat = create_features_pipeline(df)
    save_features(df_feat)