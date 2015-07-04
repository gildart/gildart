import sqlite3
db=sqlite3.connect("senac.db")
cursor=db.cursor()
cursor.execute("""
CREATE TABLE alunos(id integer primary key autoincrement,
nome varchar(100) not null,
telefone varchar(14) not null,
email varchar(100) not null unique)
""")
db.commit()
