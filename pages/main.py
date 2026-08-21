
import streamlit as st

def show():
  st.set_page_config(
    page_title="IT Learning",
    page_icon="💻",
    layout="centered"
  )

  col1, col2 = st.columns([2, 1])

  with col2:
    if st.session_state.is_login and st.session_state.log_user_name:
      st.write(f"{st.session_state.log_user_name}さん")
      if st.button("ログアウト"):
        st.session_state.is_login = False
        st.session_state.log_user_name = ""
        st.session_state.page = "main"
        st.rerun()

    else:
      col3, col4 = st.columns(2)

      with col3:
        if st.button("新規登録"):
          st.session_state.page = "register"
          st.rerun()

      with col4:
        if st.button("ログイン"):
          st.session_state.page = "login"
          st.rerun()

  st.title("IT Learning")

  st.write("IT初心者向けアプリです")

  if st.session_state.is_login and st.session_state.log_user_name:
    categories = ["Python", "SQLite", "Git"]

    for category in categories:
      if st.button(category):
        st.session_state.page = "difficulty"
        st.session_state.category = category
        st.rerun()

    

  
