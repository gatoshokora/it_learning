import streamlit as st

from AI import gemini

def show():
  st.title("IT Learning")

  st.write("IT初心者向けアプリです")

  st.subheader("問題文")
  if "questions" not in st.session_state:
    st.session_state.questions = []

  if "question_data" not in st.session_state:
    st.session_state.question_data = gemini.create_question(st.session_state.category, st.session_state.difficulty,st.session_state.questions)
    question_data = st.session_state.question_data
    st.session_state.questions.append(question_data["question"])

  st.write(question_data["question"])
  st.write("")

  st.subheader("回答")
  answer = st.radio(
    "回答を選択してください",
    question_data["choices"]
  )

  if st.button("確定"):
    if answer == "":
      st.error("回答を入力してください")
    else:
      st.session_state.page = "result"
      st.session_state.answer = answer
      if "count" not in st.session_state:
        count = 1
        st.session_state.count = count
      else:
        st.session_state.count += 1
      st.rerun()

  if st.button("戻る"):
    st.session_state.page = "difficulty"
    st.session_state.pop("question_data", None)
    st.rerun()
