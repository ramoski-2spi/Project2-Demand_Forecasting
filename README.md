# Objective
Forecast daily FIFA Ultimate Team (FUT) player card prices for the next 7 days using historical market data, event indicators, and time‑series machine learning.

# Scope
This project focuses on a subset of FUT players (e.g., 20–50 cards) to keep the data pipeline lightweight and fast. The approach can be scaled to hundreds of players.

# Forecast Horizon
The model predicts player prices 7 days into the future.

# Data Sources
- Historical FUT player prices (scraped from FUTBIN/FUTWIZ)
- FUT event calendar (TOTW, promos, SBC releases)
- Weekend league cycles (Friday–Sunday)

# Features
- Lag features (1‑day, 3‑day, 7‑day)
- Rolling averages (3‑day, 7‑day)
- Rolling volatility (std)
- Day of week
- Weekend league indicator
- Promo period indicator
- TOTW release indicator

# Modeling Approach
- Baseline model: lag‑1 forecast
- Machine learning model: XGBoost regressor
- Time‑based train/test split
- Evaluation metrics: MAPE, WAPE