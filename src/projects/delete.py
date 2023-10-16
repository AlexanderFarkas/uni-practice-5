from src.connection import db


def delete_project():
    project_id = input("ID проекта: ")
    with db() as con:
        con.execute("DELETE FROM projects WHERE id = ?", (project_id,))
        con.commit()


if __name__ == '__main__':
    delete_project()