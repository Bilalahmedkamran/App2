import streamlit as st 
import pandas
st.set_page_config(layout="wide")
st.header("The Best Company")
st.text("NVSJBVFNKVNSKBNFDKBNFKDNBKSN")
st.subheader("Our Team")

df = pandas.read_csv("data1.csv",sep=",")
col1, col2, col3 = st.columns(3)
with col1:
    for i,j in df[:4].iterrows():
        st.header((j['first name']+" "+j['last name']).title())
        st.write(j["role"])
        st.image("images1/"+j["image"])

with col2:
    for i,j in df[4:8].iterrows():
        st.header((j['first name']+" "+j['last name']).title())
        st.write(j["role"])
        st.image("images1/"+j["image"])


with col3:
    for i,j in df[8:].iterrows():
        st.header((j['first name']+" "+j['last name']).title())
        st.write(j["role"])
        st.image("images1/"+j["image"])