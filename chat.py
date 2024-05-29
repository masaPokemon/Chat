import streamlit as st

import main
import login


# 共通のsessin state ログイン情報
if 'authentication_status' not in st.session_state:
    st.session_state['authentication_status'] = None

if __name__ == "__main__":
    # ログイン認証に成功すればmain_appに切り替え
    if st.session_state['authentication_status']:
        app.app()
    else:
        obj_auth = login.Login("db/user.db")
