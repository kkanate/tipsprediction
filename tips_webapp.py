# Import packages
import streamlit as st
import joblib
import pandas as pd
from sklearn import linear_model

#Import the trained model
linregmodel = joblib.load("total_bill_size_model2.pkl")

# ── Page config ──────────────────────────────────────────────
# st.set_page_config(page_title="Tip Predictor", page_icon="🍽️")

# ── Retrain Model 2 from the tips dataset ────────────────────
#@st.cache_resource
#def load_model():
#    df = pd.read_csv("tips.csv")
#    df = df.drop_duplicates()
#    X = df[["total_bill", "size"]]
#    y = df["tip"]
#    model = linear_model.LinearRegression()
#    model.fit(X, y)
#    return model

#model = load_model()

st.title("🍽️ Tip Predictor")
st.write("Enter the bill details and the party size below to get a predicted tip amount.")

st.divider()

total_bill = st.number_input(
    "Total Bill ($)",
    min_value=0.0,
    max_value=500.0,
    value=20.0
)

party_size = st.number_input(
    "Party Size",
    min_value=1,
    max_value=20,
    value=2
)

st.divider()

if st.button("Predict Tip"):

    if total_bill == 0:
        st.warning("Please enter a bill amount greater than $0.")
    else:
        input_df = pd.DataFrame({
            "total_bill": [total_bill],
            "size": [party_size]
        })

        predicted_tip = linregmodel.predict(input_df)[0]
        predicted_tip = max(predicted_tip, 0) 
        st.success(f"Predicted Tip: ${predicted_tip:.2f}")
