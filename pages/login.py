import streamlit as st
import database

def show():
  st.subheader("ログイン画面")
  st.write("ログインするためのユーザー名とパスワードを入力してください")

  with st.form("login_form"):
    user_name = st.text_input("ユーザー名")

    password = st.text_input("パスワード", type="password")

    submit = st.form_submit_button("ログイン")

    error_message = st.empty()

    if submit :
      data = database.check_user(user_name)

      if data:
        salt = bytes.fromhex(data[0][3])
        password_hash= database.hash_password(password, salt)

        if data[0][2] == password_hash[0]:
          st.session_state.is_login = True
          st.session_state.log_user_name = data[0][1]
          st.session_state.page = "main"
          st.rerun()
        else:
          error_message.error("ユーザー名またはパスワードが違います")

      if not data:
        error_message.error("ユーザー名またはパスワードが違います")

  if st.button("戻る") :
    st.session_state.page = "main"
    st.rerun()