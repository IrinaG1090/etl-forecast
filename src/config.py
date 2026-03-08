import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
MODELS_DIR = BASE_DIR / "models"
REPORTS_DIR = BASE_DIR / "reports"

for dir_path in [DATA_DIR, MODELS_DIR, REPORTS_DIR]:
    dir_path.mkdir(exist_ok=True)

N_POINTS = 1000
TEST_SIZE = 0.2
VAL_SIZE = 0.1
RANDOM_SEED = 42

TREND_STRENGTH = 0.01
SEASONALITY_PERIOD = 30
NOISE_LEVEL = 0.05

FORECAST_HORIZON = 30
N_LAGS = 7
WINDOW_SIZE = 7

MODEL_PARAMS = {
    'xgbregressor': {
        'n_estimators': 200,
        'max_depth': 6,
        'learning_rate': 0.05,
        'subsample': 0.8,
        'colsample_bytree': 0.8,
        'random_state': RANDOM_SEED
    }
}

print("[OK] Конфигурация загружена")