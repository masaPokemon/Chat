import streamlit as st
st.title("このAIを学習させてください。")
st.text_input("")
# データベース名とテーブル名
db_name = 'datasets.db'
table_name = 'tips'

# SQLiteに書き込む
with sqlite3.connect(db_name) as conn:
    df.to_sql(table_name, conn)
