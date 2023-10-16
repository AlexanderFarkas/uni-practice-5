from getpass import getpass

from src.connection import db


def update_user():
    print("Для пропуска текущего значения оставьте поле пустым")
    user_id = int(input("ID пользователя: "))
    if not user_id:
        print("ID пользователя обязателен")
        return
    name = input("Имя пользователя: ")
    email = input("Email: ")
    password = getpass("Пароль: ")

    with db() as con:
        stmt = "UPDATE users SET "
        update_stmts = []
        if name:
            update_stmts.append(("name = ?", name))
        if email:
            update_stmts.append(("email = ?", email))
        if password:
            update_stmts.append(("password = ?", password))

        if not update_stmts:
            print("Нечего обновлять")
            return

        stmt = stmt + ", ".join([stmt for (stmt, _) in update_stmts]) + " WHERE id = ?"
        con.execute(stmt, [
            *[value for (_, value) in update_stmts],
            user_id,
        ])
        con.commit()


if __name__ == '__main__':
    update_user()