from src.connection import db


def update_task():
    print("Для пропуска текущего значения оставьте поле пустым")
    task_id = int(input("ID задачи: "))
    if not task_id:
        print("ID задачи обязателен")
        return
    name = input("Название задачи: ")
    priority = input("Приоритет: ")
    status = input("Статус: ")
    description = input("Описание: ")
    due_date = input("Дедлайн: ")
    assignee_id = int(input("ID пользователя: "))

    with db() as con:

        stmt = "UPDATE tasks SET "
        update_stmts = []
        if name:
            update_stmts.append(("name = ?", name))
        if priority:
            update_stmts.append(("priority = ?", priority))
        if status:
            update_stmts.append(("status = ?", status))
        if description:
            update_stmts.append(("description = ?", description))
        if due_date:
            update_stmts.append(("due_date = ?", due_date))
        if assignee_id:
            update_stmts.append(("assignee_id = ?", assignee_id))

        if not update_stmts:
            print("Нечего обновлять")
            return

        stmt = stmt + ", ".join([stmt for (stmt, _) in update_stmts]) + " WHERE id = ?"
        con.execute(stmt, [
            *[value for (_, value) in update_stmts],
            task_id,
        ])
        con.commit()


if __name__ == '__main__':
    update_task()