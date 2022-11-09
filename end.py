import streamlit as st
import pandas as pd
st.title("生态驾驶评分系统")
sample_df = pd.read_csv("sample1.csv")
st.write(sample_df)
vid = sample_df['vehid']
vid.drop_duplicates(subset='vehid', keep='first', inplace=False)
vid_option = st.sidebar.selectbox('choose the vehicle_id:', vid)
