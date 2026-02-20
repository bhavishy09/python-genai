import streamlit as st
import pandas as pd 
import numpy as np 

## title of application 
st.title("hello")
## display simple text 
st.write("hoi hoi ")

df =pd.DataFrame(
    {
        'first columm':[1,2,3,4],
        'first columm':[10,20,30,40]
    }
)

## display the data frame 
st.write("here the data frame")
st.write(df)


## create a line chart 
chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)

st.line_chart(chart_data)


