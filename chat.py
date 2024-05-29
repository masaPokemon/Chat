import numpy as np
import pandas as pd
import sqlite3
import seaborn as sns

from pycaret.datasets import get_data
#ボストンデータを取得
df = get_data('boston')

# データベース名とテーブル名
db_name = 'datasets.db'
table_name = 'tips'

# SQLiteに書き込む
with sqlite3.connect(db_name) as conn:
    df.to_sql(table_name, conn)
