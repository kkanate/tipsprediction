# Tip Prediction Model

A regression analysis and interactive prediction tool for estimating restaurant tips based on bill amount and party size, built using the classic Seaborn tips dataset.

## Project Overview

This project compares multiple linear regression models for predicting restaurant tips, then deploys the best-performing model as an interactive Streamlit web app. The analysis demonstrates a disciplined approach to model selection: favoring simpler models when additional complexity does not meaningfully improve predictive accuracy.

## Key Findings

- **Simpler models perform competitively.** Tested five regression models ranging from 1 to 12 features. The single-feature model (total_bill alone) achieved MAE of $0.76.
- **Two-feature model is the best tradeoff.** Adding party size as a second feature marginally improved accuracy while maintaining interpretability, making it the deployed production model.
- **Feature bloat does not help.** More complex models with 12 features showed no meaningful accuracy gains over the two-feature version, demonstrating diminishing returns.

## Tools & Technologies

- **Python** (Pandas, NumPy)
- **Scikit-learn** (Linear Regression, model comparison)
- **Streamlit** (interactive web app)
- **Joblib** (model serialization)

## Repository Contents

| File | Description |
|---|---|
| `tips_prediction _reg_analysis.ipynb` | Exploratory analysis and regression modeling notebook |
| `tips_webapp.py` | Streamlit prediction app (uses total_bill + size model) |
| `tips.csv` | Dataset (Seaborn tips dataset) |
| `total_bill_size_model2.pkl` | Deployed production model (2 features) |
| `tip_model1.pkl`, `tip_model2.pkl`, `tip_model3.pkl` | Alternative models from comparison |
| `total_bill_model1.pkl` | Single-feature baseline model |
| `variable_names.pkl` | Feature names for model inference |

## How to Run the App Locally

1. Clone this repository
2. Install dependencies: `pip install streamlit pandas scikit-learn joblib`
3. Run the app: `streamlit run tips_webapp.py`
4. The app will open in your browser at `http://localhost:8501`

## Methodology

1. **Data exploration** — Distribution analysis of tips vs. bill, party size, day of week, time, and gender
2. **Model comparison** — Trained and compared regression models with different feature combinations (1 feature, 2 features, up to 12 features with one-hot encoded categoricals)
3. **Model evaluation** — MAE, MSE, and RMSE computed on held-out test set
4. **Model selection** — Selected the simplest model whose performance was competitive with more complex alternatives
5. **Deployment** — Deployed the selected model via Streamlit for interactive tip prediction

## About

Built as part of the RND4Impact Data Analysis Program portfolio.

---

**Note:** This project is for educational and portfolio purposes only.
