import streamlit as st
import pandas as pd

st.set_page_config(page_title="MEGA-ENT ML App", layout="wide")

st.title("MEGA-ENT Streamlit ML App")
st.write("Upload OHLCV CSV data and start building the ML workflow.")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Preview")
    st.dataframe(df.head())

    required_cols = {"open", "high", "low", "close", "volume"}
    if required_cols.issubset(df.columns):
        st.success("CSV format looks correct.")
    else:
        st.error(f"Missing required columns: {required_cols - set(df.columns)}")
else:
    st.info("Upload a CSV file to begin.")
