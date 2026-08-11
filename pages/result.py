import streamlit as st


def show():
  st.subheader("結果")

  if st.session_state.question_data["answer"] == st.session_state.answer:
    st.success("正解！")

  else:
    st.error("不正解！")
    st.write(f'正解は{st.session_state.question_data["answer"]}')

  st.subheader("解説")
  st.write(st.session_state.question_data["explanation"])

  if 1 <= st.session_state.count <= 4:
    if st.button("次へ"):
      if st.session_state.question_data["answer"] == st.session_state.answer:
        if "correct" not in st.session_state:
          correct = 1
          st.session_state.correct = correct
        else :
          st.session_state.correct += 1
      st.session_state.page = "question"
      st.session_state.pop("question_data", None)
      st.session_state.pop("answer", None)
      st.rerun()

  elif st.session_state.count == 5:
    if st.button("終了"):
      if st.session_state.question_data["answer"] == st.session_state.answer:
        if "correct" not in st.session_state:
          correct = 1
          st.session_state.correct = correct
        else :
          st.session_state.correct += 1
      st.session_state.page = "finish"
      st.session_state.pop("question_data", None)
      st.session_state.pop("answer", None)

      st.rerun()

  