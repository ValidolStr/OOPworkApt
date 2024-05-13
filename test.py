import tkinter as tk
from tkinter import ttk
import sqlite3
from prettytable import PrettyTable

# Создание окна
window = tk.Tk()

# Создание таблицы
table = ttk.Treeview(window)

# Подключение к базе данных SQLite
conn = sqlite3.connect('apteka.db')
cursor = conn.cursor()

# Выполнение SQL-запроса для выборки данных
cursor.execute("SELECT * FROM users")

# Получение всех данных
rows = cursor.fetchall()

# Заполнение таблицы данными
table['columns'] = [description[0] for description in cursor.description]
table['show'] = 'headings'

for col in table['columns']:
    table.heading(col, text=col)

for row in rows:
    table.insert("", "end", values=row)

# Отображение таблицы в окне
table.pack()

# Закрытие соединения с базой данных
conn.close()

# Запуск главного цикла окна
window.mainloop()