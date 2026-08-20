import sqlite3
import hashlib
import os

#データベース接続
def connect_db():
  conn = sqlite3.connect("it_learning.db")

  return conn

#テーブル作成
def create_table():
  conn = connect_db()

  cursor = conn.cursor()

  cursor.execute("""
  CREATE TABLE IF NOT EXISTS register (
    id INTEGER PRIMARY KEY,
    user_name TEXT,
    password_hash TEXT,
    salt TEXT
  )
  """)

  conn.commit()

  conn.close()


# def add_sample():

#   conn = connect_db()

#   cursor = conn.cursor()

#   cursor.execute("""
#   INSERT INTO register 
#     (user_name, password)

#     VALUES
#     (?, ?, ?)
#   """, (
#     "test",
#     "1234"
#   ))

#   conn.commit()

#   conn.close()

def get_data():
  conn = connect_db()

  cursor = conn.cursor()

  cursor.execute("""
  SELECT * FROM register
  """)

  data = cursor.fetchall()

  conn.close()

  return data

#print(get_data())
def check_user(user_name):
  conn = connect_db()

  cursor = conn.cursor()

  cursor.execute("""
  SELECT * FROM register
  WHERE user_name = ?
  """,(user_name,))

  data = cursor.fetchall()

  conn.close()

  return data

def user_register(user_name, password):
  salt = os.urandom(16) #ランダムな値を作る 16バイト
  #ランダムな値をsaltという

  hashed_password, salt = hash_password(password, salt)
  conn = connect_db()

  cursor = conn.cursor()

  cursor.execute("""
  INSERT INTO register
      (user_name, password_hash, salt)
  VALUES
      (?, ?, ?)
  """, (
    user_name,
    hashed_password,
    salt
  ))

  conn.commit()

  conn.close()

def hash_password(password, salt):

  hashed_password = hashlib.pbkdf2_hmac(
    "sha256",     #ハッシュ化に使うアルゴリズム
    password.encode(),  #入力されたパスワードはPythonでは文字列だけどpbkdf2_hmacはバイト列を使うので変換している
    salt,
    100000    #ハッシュ計算を何回繰り返すか指定している
  )

  return hashed_password.hex(), salt.hex()

#create_table()