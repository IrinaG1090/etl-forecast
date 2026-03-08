import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import xgboost as xgb
import joblib
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
import config as cfg

def prepare_data_for_training(df, target_col='value', test_size=cfg.TEST_SIZE, val_size=cfg.VAL_SIZE):
    feature_cols = [col for col in df.columns if col not in ['timestamp', target_col]]
    X = df[feature_cols].values
    y = df[target_col].values
    n = len(df)
    n_test = int(n * test_size)
    n_val = int(n * val_size)
    n_train = n - n_test - n_val
    X_train = X[:n_train]
    y_train = y[:n_train]
    X_val = X[n_train:n_train + n_val]
    y_val = y[n_train:n_train + n_val]
    X_test = X[n_train + n_val:]
    y_test = y[n_train + n_val:]
    return X_train, X_val, X_test, y_train, y_val, y_test, feature_cols

def train_model(X_train, y_train, X_val, y_val):
    model = xgb.XGBRegressor(
        **cfg.MODEL_PARAMS['xgbregressor'],
        early_stopping_rounds=20,
        eval_metric='mae',
        verbosity=0
    )
    model.fit(X_train, y_train, eval_set=[(X_val, y_val)], verbose=50)
    return model

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    print(f"MAE: {mae:.4f}, RMSE: {rmse:.4f}, R2: {r2:.4f}")
    return y_pred

def save_model(model, feature_cols):
    model_path = cfg.MODELS_DIR / "xgboost_model.pkl"
    joblib.dump({'model': model, 'feature_cols': feature_cols}, model_path)
    print(f"[OK] Модель сохранена: {model_path}")

def save_predictions(df, y_test, y_pred):
    test_dates = df['timestamp'].iloc[-len(y_test):].values
    results_df = pd.DataFrame({'timestamp': test_dates, 'actual': y_test, 'predicted': y_pred})
    results_path = cfg.DATA_DIR / "predictions.csv"
    results_df.to_csv(results_path, index=False)
    print(f"[OK] Предсказания сохранены: {results_path}")

if __name__ == "__main__":
    df = pd.read_csv(cfg.DATA_DIR / "features_data.csv", parse_dates=['timestamp'])
    X_train, X_val, X_test, y_train, y_val, y_test, feature_cols = prepare_data_for_training(df)
    model = train_model(X_train, y_train, X_val, y_val)
    y_pred = evaluate_model(model, X_test, y_test)
    save_model(model, feature_cols)
    save_predictions(df, y_test, y_pred)