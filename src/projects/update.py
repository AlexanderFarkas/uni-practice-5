from src.connection import db


def update_project():
    project_id = input("ID проекта: ")
    name = input("Название проекта: ")
    with db() as con:
        con.execute("UPDATE projects SET name = ? WHERE id = ?", (name, project_id))
        con.commit()


if __name__ == '__main__':
    update_project()