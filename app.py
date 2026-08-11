import streamlit as st

from pages import main
from pages import difficulty
from pages import question
from pages import result
from pages import finish


if "page" not in st.session_state:
  st.session_state.page = "main"

if "category" not in st.session_state:
  st.session_state.category = ""

if "difficulty" not in st.session_state:
  st.session_state.difficulty = ""

if "answer" not in st.session_state:
  st.session_state.answer = ""



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
  