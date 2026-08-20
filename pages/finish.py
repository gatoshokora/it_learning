import streamlit as st

def show():
  st.title("IT Learning")

  st.write("IT初心者向けアプリです")

  st.subheader("結果")
  st.write(f"{st.session_state.count}問中{st.session_state.correct}問正解です。")

  if st.button("ホーム画面へ"):
    st.session_state.pop("count", None)
    st.session_state.pop("correct", None)
    st.session_state.pop("questions", None)
    st.session_state.page = "main"
    st.rerun()