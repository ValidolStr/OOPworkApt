import flet as ft
import sqlite3

conn = sqlite3.connect('apteka.db')
cursor = conn.cursor()

# Получение данных из таблицы
cursor.execute("SELECT * FROM users")
data = cursor.fetchall()

# Создание заголовков колонок
columns = [ft.DataColumn(ft.Text(header[0])) for header in cursor.description]

# Добавление столбца с кнопкой "Удалить"
columns.append(ft.DataColumn(ft.Text("Действия")))

# Создание DataTable
table = ft.DataTable(
    columns=columns,
    rows=[
        ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(str(cell)), on_tap=lambda e, row_id=row[0], col_index=i: выбрать_ячейку(e, row_id, col_index))
                for i, cell in enumerate(row)
            ] + [
                ft.DataCell(ft.ElevatedButton(text="Удалить", on_click=lambda e, row_id=row[0]: удалить_строку(e, row_id)))
            ]
        )
        for row in data
    ]
)

# Текстовые поля для отображения данных
text_field_1 = ft.TextField(label="Значение 1", read_only=True)
text_field_2 = ft.TextField(label="Значение 2", read_only=True)

# Функция для выбора ячейки
def выбрать_ячейку(e, row_id, col_index):
    # Получение значения из выбранной ячейки
    value = data[row_id][col_index]

    # Обновление текстовых полей
    if col_index == 0:
        text_field_1.value = str(value)
    elif col_index == 1:
        text_field_2.value = str(value)
    text_field_1.update()
    text_field_2.update()

# Функция для удаления строки
def удалить_строку(e, id):
    # Удаление строки из базы данных
    cursor.execute("DELETE FROM users WHERE id = ?", (id,))
    conn.commit()

    # Обновление DataTable
    table.rows = [
        ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(str(cell)), on_tap=lambda e, row_id=row[0], col_index=i: выбрать_ячейку(e, row_id, col_index))
                for i, cell in enumerate(row)
            ] + [
                ft.DataCell(ft.ElevatedButton(text="Удалить", on_click=lambda e, row_id=row[0]: удалить_строку(e, row_id)))
            ]
        )
        for row in cursor.execute("SELECT * FROM users").fetchall()
    ]
    page.update()

# Функция для обновления данных в таблице
def обновить_таблицу(e):
        # Получение новых значений из текстовых полей
        new_value_1 = text_field_1.value
        new_value_2 = text_field_2.value

        # Обновление данных в базе данных
        # ... (ваш код обновления данных в базе данных)

        # Обновление DataTable
        table.rows = [
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(cell)), on_tap=lambda e, row_id=row[0], col_index=i: выбрать_ячейку(e, row_id, col_index))
                    for i, cell in enumerate(row)
                ] + [
                    ft.DataCell(ft.ElevatedButton(text="Удалить", on_click=lambda e, row_id=row[0]: удалить_строку(e, row_id)))
                ]
            )
            for row in cursor.execute("SELECT * FROM users").fetchall()
        ]
        page.update()

# Создание страницы Flet
page = ft.Page()

# Добавление элементов на страницу
page.add(
        ft.Column(
            [
                table,
                ft.Row(
                    [
                        text_field_1,
                        text_field_2,
                        ft.ElevatedButton(text="Обновить", on_click=обновить_таблицу),
                    ]
                ),
            ]
        )
    )

ft.app(target=page)