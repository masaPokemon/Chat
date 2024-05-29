import streamlit as st
import sqlite3
import pandas as pd
import main
main.input()
#先ほど設定したDBの名前
db_name = 'datasets.db'

select_all_sql = 'select ' + '*' + ' from ' + 'tips'
with sqlite3.connect(db_name) as conn:
    df_from_sql = pd.read_sql(select_all_sql, conn)

#列名を取り出す
df_from_sql_columns = df_from_sql.columns

#####stゾーン開始

option = st.selectbox(
    'どの列がはいっているデータを抽出しますか？',
    (df_from_sql_columns)
)

num = st.text_input('数字を半角で入力してください :例 0.04')
#列と入力値両方が入力されるまで待つためのif文
if not option or not num:
  st.title("列と数字が入力されるまで待ちます")
else:
  st.title("選択されました")
  def sql1(columns, num2):
    sql = 'select ' + '*' + ' from ' + 'tips' + ' where ' + columns + ' > ' + num2
    return sql
  sql2 = sql1(option, num)
  with sqlite3.connect(db_name) as conn:
      df_from_sql2 = pd.read_sql(sql2, conn)
  st.dataframe(df_from_sql2)
#####stゾーン終了
