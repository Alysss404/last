import streamlit as st
import pandas as pd
sample_df = pd.read_csv("sample1.csv")
st.write(sample_df)
