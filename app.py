import streamlit as st
import numpy as np
import pandas as pd
import sqlite3

con = sqlite3.connect('test.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS comments (com)''')

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
comments = cur.execute('SELECT * FROM comments').fetchall()
file.close()
textfile = open("comments.txt", "a")
comment = st.text_input('Input your comment:') 
if comment:
    comments.append(comment)
    cur.execute("INSERT INTO comments VALUE ('%s')" % comment)

st.write(comments)
con.close()
