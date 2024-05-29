import sqlite3
import streamlit as st
user = st.text_input("name")
# データベースに接続する
conn = sqlite3.connect('ChatData.db')
c = conn.cursor()
st.title("Echo Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in c:
    st.markdown(c)

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": user, "content": prompt})
    c += prompt
    conn.commit()
