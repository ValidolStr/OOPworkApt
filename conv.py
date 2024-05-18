# import tkinter as tk
# from tkinter import ttk
# import sqlite3


# def add_supplier():
#     # Получение данных из полей ввода
#     new_name = name_entry.get()
#     new_price = price_entry.get()
#     new_pacing = pacing_entry.get()
#     new_quantity = quantity_entry.get()
#     new_posta = posta_entry.get()
    
#     # ... (получение других данных о поставщике)

#     # Проверка введенных данных (необязательно, но рекомендуется)
#     if not new_name:
#         # Вывод сообщения об ошибке, если имя поставщика не введено
#         tk.messagebox.showerror("Ошибка", "Введите имя поставщика")
#         return

#     # Подключение к БД
#     conn = sqlite3.connect("db_name")
#     cursor = conn.cursor()

#     # Вставка данных в БД
#     try:
#         cursor.execute(
#             "INSERT INTO products (name, price, quantity, packing, pospav_id) VALUES (?, ?, ?, ?, ?)",
#             (new_name, new_price, new_quantity, new_pacing, new_posta),
#         )
#         conn.commit()
#         tk.messagebox.showinfo("Успешно", "Товавр добавлен")
#     except Exception as e:
#         tk.messagebox.showerror("Ошибка", f"Ошибка добавления поставщика: {e}")
#     finally:
#         conn.close()

#     # Обновление списка поставщиков (необязательно, но рекомендуется)
#     # ... (код для обновления списка поставщиков)

# # Поля ввода для данных нового поставщика
# name_label = tk.Label(goods_window, text="Имя поставщика:")
# name_label.pack(pady=10)
# name_entry = tk.Entry(goods_window)
# name_entry.pack(pady=10)

# price_label = tk.Label(goods_window, text="Имя поставщика:")
# price_label.pack(pady=10)
# price_entry = tk.Entry(goods_window)
# price_entry.pack(pady=10)

# pacing_label = tk.Label(goods_window, text="Имя поставщика:")
# pacing_label.pack(pady=10)
# pacing_entry = tk.Entry(goods_window)
# pacing_entry.pack(pady=10)

# quantity_label = tk.Label(goods_window, text="Имя поставщика:")
# quantity_label.pack(pady=10)
# quantity_entry = tk.Entry(goods_window)
# quantity_entry.pack(pady=10)

# posta_label = tk.Label(goods_window, text="Имя поставщика:")
# posta_label.pack(pady=10)
# posta_entry = tk.Entry(goods_window)
# posta_entry.pack(pady=10)
# # ... (добавьте поля ввода для других данных о поставщике)

# # Кнопка "Добавить"
# add_button = tk.Button(goods_window, text="Добавить", command=add_supplier, width=20, height=5)
# add_button.pack(pady=20) 