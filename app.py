import streamlit as st

from pages import main
from pages import difficulty
from pages import question
from pages import result
from pages import finish
from pages import register
from pages import regi_confirm
from pages import login


if "page" not in st.session_state:
  st.session_state.page = "main"

if "category" not in st.session_state:
  st.session_state.category = ""

if "difficulty" not in st.session_state:
  st.session_state.difficulty = ""

if "answer" not in st.session_state:
  st.session_state.answer = ""

if "is_login" not in st.session_state:
  st.session_state.is_login = False

if "log_user_name" not in st.session_state:
  st.session_state.log_user_name = ""


if st.session_state.page == "main":
  main.show()

elif st.session_state.page == "difficulty":
  difficulty.show()

elif st.session_state.page == "question":
  question.show()

elif st.session_state.page == "result":
  result.show()

elif st.session_state.page == "finish":
  finish.show()

elif st.session_state.page == "register":
  register.show()

elif st.session_state.page == "regi_confirm":
  regi_confirm.show()

elif st.session_state.page == "login":
  login.show()