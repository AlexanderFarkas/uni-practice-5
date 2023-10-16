from src.connection import db


def create_project():
    name = input("Название проекта: ")
    with db() as con:
        cursor = con.execute("INSERT INTO projects (name) VALUES (?) RETURNING id", (name,))
        print(f"ID: {cursor.fetchone()[0]}")
        con.commit()


if __name__ == '__main__':
    create_project()
