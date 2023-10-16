from getpass import getpass

from src.connection import db


def create_user():
    name = input("Имя пользователя: ")
    email = input("Email: ")
    password = getpass("Пароль: ")

    with db() as con:
        cursor = con.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?) RETURNING id", (name, email, password))
        print(f"ID: {cursor.fetchone()[0]}")
        con.commit()

if __name__ == '__main__':
    create_user()