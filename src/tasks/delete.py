from src.connection import db


def delete_user():
    user_id = input("ID задачи: ")
    with db() as con:
        con.execute("DELETE FROM users WHERE id = ?", (user_id,))
        con.commit()


if __name__ == '__main__':
    delete_user()