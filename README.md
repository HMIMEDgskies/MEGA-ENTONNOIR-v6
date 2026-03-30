# MEGA-ENTONNOIR-v6
# MEGA-ENTONNOIR-v6

A Streamlit-based machine learning app for OHLCV market data.

## What this app does

- Uploads OHLCV CSV data
- Validates required trading columns
- Prepares the base for feature engineering and ML workflows
- Runs as a Streamlit app deployed from GitHub

## Required files in this repository

- `README.md`
- `app.py`
- `requirements.txt`

## Required CSV columns

Your uploaded CSV should contain:

- `open`
- `high`
- `low`
- `close`
- `volume`

Optional columns:

- `timestamp`
- `date`

## Run locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

1. Connect your GitHub repository
2. Select the correct repository
3. Set branch to `main`
4. Set main file path to `app.py`
5. Click **Deploy**

## Notes

This repository is the base structure for a larger MEGA-ENT ML dashboard that will later include:
- feature engineering,
- model training,
- signal generation,
- backtesting,
- probability output,
- trading workflow integration.
