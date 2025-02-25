import sqlite3

conn = sqlite3.connect("dados.db")
cursor = conn.cursor()

def create_table():
    try:
        conn.execute("CREATE TABLE users(NAME TEXT, AGE INTEGER, EMAIL TEXT)")
        conn.commit()
        conn.close()
        print("Tabela criada com sucessso")
    except sqlite3.Error as erro:
        print("Erro em -->" + erro)
# create_table()

def add():
    name = input("Digite seu nome : ")
    age = input("Digite sua idade : ")
    email = input("Digite seu email : ")
    try:
        conn.execute("INSERT INTO users VALUES('"+ name +"', '"+ age +"', '"+ email +"')")
        conn.commit()
        conn.close()
        print("Registro salvo com sucesso")
    except sqlite3.Error as erro:
        print("Erro em -->" + erro)
# add()

def info():
    result = conn.execute("SELECT * FROM users")
    print(result.fetchall())
# info()