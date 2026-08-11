import streamlit as st

def show():
  st.title("IT Learning")

  st.write("IT初心者向けアプリです")


  st.write(f"{st.session_state.category}の難易度を選択してください")

  levels = {
    "初級": "easy",
    "中級": "normal",
    "上級": "hard"
    }

  for label, value in levels.items():
    if  st.button(label):
      st.session_state.difficulty = value
      st.session_state.page = "question"
      st.rerun() 

  if st.button("戻る"):
    st.session_state.page = "main"
    st.session_state.category = ""
    st.session_state.difficulty = ""
    st.rerun()