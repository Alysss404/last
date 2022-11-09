import streamlit as st
import pandas as pd
st.title("生态驾驶评分系统")
sample_df = pd.read_csv("sample1.csv")
st.write(sample_df)
vid = sample_df['vehid']
vid.drop_duplicates(keep='first', inplace=True)
vid_option = st.sidebar.selectbox('choose the vehicle_id:', vid)


# oid = sample_df[['vehid']=='{}'].format(vid_option)
# st.write(oid)
oid = sample_df['orderid']
oid.drop_duplicates(keep='first', inplace=True)
oid_option = st.sidebar.selectbox('choose the order_id:', oid)

option_df = sample_df['vehid' == '{}','orderid' == '{}'].format(vid_option,oid_option)
st.write(option_df)
st.map(option_df)
