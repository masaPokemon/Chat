import sqlite3
import streamlit as st

# データベースに接続する
conn = sqlite3.connect('ChatData.db')
c = conn.cursor()

# Display chat messages from history on app rerun
for message in c:
    st.markdown(c)

# React to user input
if prompt := st.chat_input("message"):
    c.execute(user, prompt)
    conn.commit
