import streamlit as st
import database


def show():
  st.write("新規登録画面です。ユーザー名とパスワードを入力してください。")

  with st.form("register_form"):
    user_name = st.text_input("ユーザー名")
    error_message = st.empty()

    password = st.text_input("パスワード", type="password")
    p_error_message = st.empty()

    submit = st.form_submit_button("確認")

  if submit:
    data = database.check_user(user_name)

    user_error = False

    if data:
      error_message.error("すでに使われているユーザー名です")
      user_error = True
    
    if not data:
      st.session_state.user_name = user_name

    password_error = False

    if (
      len(password) >= 8
      and password.isascii()
      and password.isalnum()
      and any(char.isupper() for char in password)
      and any(char.islower() for char in password)
      and any(char.isdigit() for char in password)
    ):

      st.session_state.password = password

    else:
      p_error_message.error("半角英数字（大文字、小文字、数字）を含む8文字以上にして下さい")
      password_error = True

    if not user_error and not password_error:
      st.session_state.page = "regi_confirm"
      st.rerun()

  if st.button("戻る"):
    st.session_state.pop("user_name", None)
    st.session_state.pop("password", None)
    st.session_state.page = "main"
    st.rerun()