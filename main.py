import sqlite3
import pandas as pd

#先ほど設定したDBの名前
db_name = 'datasets.db'

select_all_sql = 'select ' + '*' + ' from ' + 'tips'
with sqlite3.connect(db_name) as conn:
    df_from_sql = pd.read_sql(select_all_sql, conn)

#列名を取り出す
df_from_sql_columns = df_from_sql.columns
