import streamlit as st
import mysql.connector

### ファイル読み込み
 
### DB接続
cnx = mysql.connector.connect(host='localhost', user='root', password='', database='user.db')
cnx2 = mysql.connector.connect(host='localhost', user='root', password='', database='ChatData.db')
 
### カーソル作成
cursor = cnx.cursor()

### カーソル作成
cursor2 = cnx.cursor() 

### INSERT文作成
sql = "INSERT INTO weather_forecast ( date_time, pressure, temperature, humidity) VALUES (%s, %s, %s, %s)"

user = st.text_input("name")
# データベースに接続する
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
    
    ### データ挿入実行
    cursor.execute()
    conn.commit()


### コミット
cnx.commit()
 
### カーソルクローズ
cursor.close()
