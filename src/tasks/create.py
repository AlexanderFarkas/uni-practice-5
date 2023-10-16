from getpass import getpass

from src.connection import db


def create_task():
    name = input("Название задачи: ")
    project_id = int(input("ID проекта: "))

    with db() as con:
        cursor = con.execute("INSERT INTO tasks (name, project_id) VALUES (?, ?) RETURNING id", (name, project_id))
        print(f"ID: {cursor.fetchone()[0]}")
        con.commit()

if __name__ == '__main__':
    create_task()