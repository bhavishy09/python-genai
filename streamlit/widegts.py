import streamlit as st
import pandas as pd 
from PIL import Image
st.title("widegts")

name=st.text_input("enter your name:")


age =st.slider("select your age :",0,50,18)
st.write(f"your age is :{age}")

option=["java",'c++',"sql"]

choice=st.selectbox("choose your fav language:",option)
st.write(f"select lang is :{choice}")

if name:
    st.write(f"helo {name}")



data={
    "name":["bhavishya","rohit"],
    "age":["20","30"]
}

df=pd.DataFrame(data)
df.to_csv("sample.csv")
st.write(df)
  
upload_file=st.file_uploader("choose png file:",type="png")

if upload_file is not None :
    image = Image.open(upload_file)   # open with Pillow
    st.image(image, caption="Uploaded Image", use_column_width=True)

