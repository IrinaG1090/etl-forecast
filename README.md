# 📈 ETL & Time-Series Forecasting Pipeline

[![Python](https://img.shields.io/badge/python-3.12-blue)](https://www.python.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-2.1.4-orange)](https://xgboost.readthedocs.io/)
[![Pandas](https://img.shields.io/badge/pandas-2.2.3-green)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📝 О проекте

**ETL & Forecasting Pipeline** — это полноценный, production-ready пайплайн для обработки временных рядов и построения прогнозных моделей. Проект является пятым этапом большого плана по созданию end-to-end AI систем и демонстрирует фундаментальные навыки Data Engineering и MLOps.

### ✨ Возможности

- 📊 **Генерация данных** — создание синтетических временных рядов с трендом, сезонностью и шумом
- 🧹 **ETL-процесс** — очистка данных, обработка пропусков, удаление выбросов
- 🔧 **Инженерия признаков** — создание лагов, скользящих средних, признаков даты
- 🤖 **Обучение модели** — XGBoost регрессор с валидацией и ранней остановкой
- 📉 **Визуализация** — графики предсказаний, остатков, важности признаков
- 🚀 **Модульная архитектура** — каждый этап пайплайна изолирован в отдельный скрипт

## 🛠️ Технологический стек

| Компонент | Технология |
|-----------|------------|
| **Язык** | Python 3.12 |
| **Обработка данных** | Pandas, NumPy |
| **Инженерия признаков** | Pandas |
| **Модель** | XGBoost (с ранней остановкой) |
| **Валидация** | TimeSeriesSplit |
| **Визуализация** | Matplotlib, Seaborn |
| **Метрики** | MAE, RMSE, R² |

## 📋 Предварительные требования

- Python 3.12+
- Git (для клонирования)

## 🚀 Быстрый старт

### 1. Клонировать репозиторий

```bash
git clone https://github.com/IrinaG1090/etl-forecast.git
cd etl-forecast
```

### 2. Создать виртуальное окружение

```bash
python -m venv venv_etl
source venv_etl/bin/activate  # для Linux/Mac
.\venv_etl\Scripts\Activate.ps1   # для Windows
```

### 3. Установить зависимости

```bash
pip install pandas numpy scikit-learn xgboost matplotlib seaborn jupyter
```

Или через requirements.txt:
```bash
pip install -r requirements.txt
```

### 4. Запустить полный пайплайн

```bash
python src/main.py
```

## 📁 Структура проекта

```bash
etl-forecast/
├── src/
│   ├── config.py              # Централизованные настройки
│   ├── generate_data.py        # Генерация синтетических данных
│   ├── etl.py                  # Очистка и подготовка
│   ├── features.py              # Инженерия признаков
│   ├── train.py                 # Обучение XGBoost
│   ├── evaluate.py              # Визуализация результатов
│   └── main.py                  # Оркестратор пайплайна
├── data/                         # Сгенерированные данные
│   ├── raw_data.csv
│   ├── cleaned_data.csv
│   ├── features_data.csv
│   └── predictions.csv
├── models/                        # Сохранённые модели
│   └── xgboost_model.pkl
├── reports/                        # Графики и отчёты
│   ├── predictions_plot.png
│   ├── residuals_plot.png
│   └── feature_importance.png
├── .gitignore
├── requirements.txt
└── README.md
```

## 🧪 Этапы пайплайна

| Этап | Скрипт | Описание | Результат |
|:---|:---|:---|:---|
| **1. Генерация** | `generate_data.py` | Создание временного ряда с трендом, сезонностью и шумом | `data/raw_data.csv` |
| **2. ETL** | `etl.py` | Очистка данных, обработка пропусков | `data/cleaned_data.csv` |
| **3. Фичи** | `features.py` | Лаги, скользящие средние, признаки даты | `data/features_data.csv` |
| **4. Обучение** | `train.py` | XGBoost с TimeSeriesSplit | `models/xgboost_model.pkl` + `data/predictions.csv` |
| **5. Визуализация** | `evaluate.py` | Графики и анализ важности признаков | `reports/*.png` |

## 📊 Примеры визуализаций

Предсказания vs Факт
https://reports/predictions_plot.png

Анализ остатков
https://reports/residuals_plot.png

Важность признаков
https://reports/feature_importance.png

## 🤝 Вклад в проект
Буду рада любым предложениям и улучшениям! Создавайте issue или отправляйте pull request.

## 📄 Лицензия
Проект распространяется под лицензией MIT. Подробнее в файле LICENSE.

## 🙏 Благодарности
XGBoost за отличный алгоритм градиентного бустинга

Сообществу Pandas за мощные инструменты обработки данных

## Сделано с ❤️