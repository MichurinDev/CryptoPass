import sqlite3 as SQL

db = SQL.connect("PasswordManagerDB.db")
sql = db.cursor()
db_name = "PasswordManager"

sql.execute(f"""CREATE TABLE IF NOT EXISTS {db_name} (
    web TEXT,
    login TEXT,
    password TEXT
)""")

db.commit()

user_web = input('Web: ')
user_login = input('Login: ')
user_password = input('Password: ')

sql.execute(f"SELECT login FROM {db_name}")
for web, login, _ in sql.execute(f"SELECT * FROM {db_name}"):
    if login == user_login and web == user_web:
        print(f'Пользователь "{login}" на сервисе "{web}" уже присутсвует в базе!')
        break
else:
    sql.execute(f"INSERT INTO {db_name} VALUES (?, ?, ?)", (user_web, user_login, user_password))
    db.commit()

print('-------')
for value in sql.execute(f"SELECT * FROM {db_name}"):
    print(*value, sep='\t')