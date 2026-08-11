
import streamlit as st

def show():
  st.set_page_config(
    page_title="IT Learning",
    page_icon="💻",
    layout="centered"
  )

  st.title("IT Learning")

  st.write("IT初心者向けアプリです")

  categories = ["Python", "SQLite", "Git"]

  for category in categories:
    if st.button(category):
      st.session_state.page = "difficulty"
      st.session_state.category = category
      st.rerun()
    

  
