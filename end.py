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

# option_df = sample_df['vehid' == '{}','orderid' == '{}'].format(vid_option,oid_option)
# option_df = sample_df[sample_df['vehid' == 2,'orderid' == 4551]]
option_df = sample_df[(sample_df['vehid']==‘2’)&(sample_df['orderid']==‘4551’)]
st.write(option_df)
st.map(option_df)

st.header("评分")
st.text("该车辆对应订单驾驶行为分析及其分数：")
score_df = pd.read_csv("score3.csv")
score = score_df[score_df['orderid']==‘4551’]
st.write(score_df)
expander = st.expander("添加新的数据")
with expander:

    uploaded_files = st.file_uploader("请选择一个CSV文件", accept_multiple_files=True)
    uploaddf = pd.DataFrame()
    for uploaded_file in uploaded_files:
        uploaddf = pd.read_csv(uploaded_file)

        st.write(uploaddf)
    if st.button('上传到数据库'):
        st.success("上传成功!")
