import streamlit as st
import numpy as np
import pandas as pd


df = pd.read_csv('season-1819_csv.csv')
df.head()
sl= st.slider('Row?', 0, df.index[-1], 25)
st.title('Counters POG')
if 'count' not in st.session_state:
    st.session_state.count = 0

increment = st.button('Increment')
if increment:
    st.session_state.count += 1

st.write('Count = ', st.session_state.count)

st.write(df.iloc[sl:sl+1])
file = open('comments.txt', 'r')
comments = file.readlines()
file.close()
textfile = open("comments.txt", "w")
comment = st.text_input('Input your comment:') 
if comment:
    comments.append(comment)
    textfile.write(comment + '\n')

st.write(comments)