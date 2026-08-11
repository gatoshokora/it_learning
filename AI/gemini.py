import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import json


load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def create_question(category, difficulty):

  levels = {
    "easy": "初級",
    "normal": "中級",
    "hard": "上級"
  }

  level = levels[difficulty]
      
  response = client.models.generate_content(
    model='gemini-3.5-flash',
    contents=f"""
    {category}の{level}問題を1問出してください。

    以下のJSON形式で返してください。
    answerには正解の選択肢の文字列をそのまま入れてください。
    {{
      "question" : "",
      "type" : "choice",
      "choices" : [],
      "answer" : "",
      "explanation" : ""
    }}
    """,
    config=types.GenerateContentConfig(
      response_mime_type="application/json"
    )
  )
  #print(response.text)
  data = json.loads(response.text)
  return data

