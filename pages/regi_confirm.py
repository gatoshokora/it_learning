import streamlit as st
import database

def show():
  st.write("確認画面です。登録はまだ完了していません。")

  st.subheader("ユーザー名")
  st.write(st.session_state.user_name)

  st.subheader("パスワード")
  pass_count = len(st.session_state.password)
  st.write("●" * pass_count)

  st.write("この内容で登録しますか？")
  if st.button("登録"):
    database.user_register(st.session_state.user_name, st.session_state.password)
    st.session_state.pop("user_name", None)
    st.session_state.pop("password", None)
    st.session_state.page = "main"

  if st.button("戻る"):
    st.session_state.page = "register"
    st.rerun()