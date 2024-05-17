import tkinter as tk
from tkinter import ttk
import sqlite3

def open_cabinet_window():
    global root
    root.withdraw()
    cabinet_window = tk.Toplevel(root)
    cabinet_window.title("Кабинет")
    cabinet_window.geometry("800x700")

    def close_cabinet_window():
        cabinet_window.destroy()
        root.deiconify()

def open_cabinet_window():
    global root
    root.withdraw()
    cabinet_window = tk.Toplevel(root)
    cabinet_window.title("Кабинет")
    cabinet_window.geometry("500x400")

    def close_cabinet_window():
        cabinet_window.destroy()
        root.deiconify()

    # Замена данных из базы данных на статические значения
    pharmacy_data = {
        "UNP": "123456789",
        "Юридический адрес": "ул. Ленина, д. 1",
        "Email": "apteka@example.com",
        "Телефон": "+375 123 456 789",
        "Название": "Аптека №1"
    }

    # Отображение информации об аптеке
    info_frame = tk.Frame(cabinet_window)
    info_frame.pack(pady=50)

    # Создание метки с информацией
    info_text = f"УНП: {pharmacy_data['UNP']}\n" \
                f"Юридический адрес: {pharmacy_data['Юридический адрес']}\n" \
                f"Email: {pharmacy_data['Email']}\n" \
                f"Телефон: {pharmacy_data['Телефон']}\n" \
                f"Название: {pharmacy_data['Название']}"
    info_label = tk.Label(info_frame, text=info_text, font=("Arial", 12), justify="left")
    info_label.pack()

    # Кнопка "Назад"
    back_button = tk.Button(cabinet_window, text="Назад", command=close_cabinet_window, width=20, height=5)
    back_button.pack(pady=50)

    def delete_selected_row():
        selected_item = tree.selection()
        if selected_item:
            # Получение ID выбранной строки
            user_id = tree.item(selected_item[0])['values'][0]  # Предполагается, что ID - первый столбец

            # Подключение к базе данных
            conn = sqlite3.connect("apteka.db")
            cursor = conn.cursor()

            # Удаление записи из таблицы users
            try:
                cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
                conn.commit()
                tree.delete(selected_item)  # Удаление строки из Treeview
                print(f"Строка с ID {user_id} удалена из таблицы users.")
            except Exception as e:
                print(f"Ошибка при удалении строки: {e}")

            # Закрытие соединения с базой данных
            conn.close()

    # Подключение к базе данных
    conn = sqlite3.connect("apteka.db")
    cursor = conn.cursor()

    # Получение данных из таблицы users
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    # Создание фрейма для таблицы
    table_frame = tk.Frame(cabinet_window)
    table_frame.pack(pady=50)

    # Создание Treeview
    tree = ttk.Treeview(table_frame, columns=[column[0] for column in cursor.description], show="headings")
    tree.pack(side="left", fill="both", expand=True)

    # Заголовки столбцов
    for i, column in enumerate(cursor.description):
        tree.heading(column[0], text=column[0])
        tree.column(column[0], anchor="w", width=100, stretch=True)  # Выравнивание по левому краю

    # Данные таблицы
    for row in users:
        tree.insert("", "end", values=row)

    # Создание скроллбаров
    scrollbar_y = tk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
    scrollbar_y.pack(side="right", fill="y")
    scrollbar_x = tk.Scrollbar(table_frame, orient="horizontal", command=tree.xview)
    scrollbar_x.pack(side="bottom", fill="x")

    # Связывание скроллбаров с Treeview
    tree.config(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

    # Закрытие соединения с базой данных
    conn.close()

def open_goods_window():
    global root
    root.withdraw()
    goods_window = tk.Toplevel(root)
    goods_window.title("Товары")
    goods_window.geometry("800x700")

    def close_goods_window():
        goods_window.destroy()
        root.deiconify()

    def delete_selected_row():
        selected_item = tree.selection()
        if selected_item:
            # Получение ID выбранной строки
            product_id = tree.item(selected_item[0])['values'][0]  # Предполагается, что ID - первый столбец

            # Подключение к базе данных
            conn = sqlite3.connect("apteka.db")
            cursor = conn.cursor()

            # Удаление записи из таблицы products
            try:
                cursor.execute("DELETE FROM products WHERE id=?", (product_id,))
                conn.commit()
                tree.delete(selected_item)  # Удаление строки из Treeview
                print(f"Строка с ID {product_id} удалена из таблицы products.")
            except Exception as e:
                print(f"Ошибка при удалении строки: {e}")

            # Закрытие соединения с базой данных
            conn.close()

    def search_products(event=None):
        search_term = search_entry.get()
        if search_term:
            # Подключение к базе данных
            conn = sqlite3.connect("apteka.db")
            cursor = conn.cursor()

            # Поиск в базе данных
            cursor.execute("SELECT * FROM products WHERE name LIKE ?", ('%' + search_term + '%',))
            products = cursor.fetchall()

            # Очистка существующих данных в Treeview
            tree.delete(*tree.get_children())

            # Добавление найденных продуктов в Treeview
            for row in products:
                tree.insert("", "end", values=row)

            # Закрытие соединения с базой данных
            conn.close()
        else:
            # Очистка существующих данных в Treeview
            tree.delete(*tree.get_children())

            # Подключение к базе данных
            conn = sqlite3.connect("apteka.db")
            cursor = conn.cursor()

            # Получение всех товаров
            cursor.execute("SELECT * FROM products")
            products = cursor.fetchall()

            # Добавление всех товаров в Treeview
            for row in products:
                tree.insert("", "end", values=row)

            # Закрытие соединения с базой данных
            conn.close()

    def calculate_total_cost():
        global root
        root.withdraw()
        total_cost_window = tk.Toplevel(root)
        total_cost_window.title("Сумарная стоимость товаров")
        total_cost_window.geometry("400x200")

        def close_total_cost_window():
            total_cost_window.destroy()
            #root.deiconify()

        # Подключение к базе данных
        conn = sqlite3.connect("apteka.db")
        cursor = conn.cursor()

        # Получение сумарной стоимости товаров
        cursor.execute("SELECT SUM(price * quantity) FROM products")
        total_cost = cursor.fetchone()[0]

        # Отображение сумарной стоимости
        total_cost_label = tk.Label(total_cost_window, text=f"Сумарная стоимость: {total_cost}", font=("Arial", 14))
        total_cost_label.pack(pady=50)

        # Кнопка "Назад"
        back_button = tk.Button(total_cost_window, text="Назад", command=close_total_cost_window, width=20, height=5)
        back_button.pack(pady=20)

        # Закрытие соединения с базой данных
        conn.close()

    def edit_selected_row():
        selected_item = tree.selection()
        if selected_item:
            # Получение ID выбранной строки
            product_id = tree.item(selected_item[0])['values'][0]

            # Получение текущих значений строки
            current_values = tree.item(selected_item[0])['values']

            # Создание окна редактирования
            edit_window = tk.Toplevel(goods_window)
            edit_window.title("Редактирование товара")
            edit_window.geometry("500x500")

            # Поля для ввода
            name_label = tk.Label(edit_window, text="Название:")
            name_label.grid(row=0, column=0, padx=5, pady=5)
            name_entry = tk.Entry(edit_window, width=50)
            name_entry.insert(0, current_values[1])  # Заполняем поле ввода текущим значением
            name_entry.grid(row=0, column=1, padx=5, pady=5)

            price_label = tk.Label(edit_window, text="Цена:")
            price_label.grid(row=1, column=0, padx=5, pady=5)
            price_entry = tk.Entry(edit_window, width=50)
            price_entry.insert(0, current_values[3])
            price_entry.grid(row=1, column=1, padx=5, pady=5)

            pacing_label = tk.Label(edit_window, text="Фасовка:")
            pacing_label.grid(row=2, column=0, padx=5, pady=5)
            pacing_entry = tk.Entry(edit_window, width=50)
            pacing_entry.insert(0, current_values[2])
            pacing_entry.grid(row=2, column=1, padx=5, pady=5)
            
            quantity_label = tk.Label(edit_window, text="Количество:")
            quantity_label.grid(row=3, column=0, padx=5, pady=5)
            quantity_entry = tk.Entry(edit_window, width=50)
            quantity_entry.insert(0, current_values[5])
            quantity_entry.grid(row=3, column=1, padx=5, pady=5)
            
            posta_label = tk.Label(edit_window, text="Поставщик:")
            posta_label.grid(row=4, column=0, padx=5, pady=5)
            posta_entry = tk.Entry(edit_window, width=50)
            posta_entry.insert(0, current_values[4])
            posta_entry.grid(row=4, column=1, padx=5, pady=5)
            
            srok_label = tk.Label(edit_window, text="Срок годности:")
            srok_label.grid(row=5, column=0, padx=5, pady=5)
            srok_entry = tk.Entry(edit_window, width=50)
            srok_entry.insert(0, current_values[6])
            srok_entry.grid(row=5, column=1, padx=5, pady=5)

            # Кнопка сохранения изменений
            def save_changes():
                # Получение новых значений из полей ввода
                new_name = name_entry.get()
                new_price = price_entry.get()
                new_pacing = pacing_entry.get()
                new_quantity = quantity_entry.get()
                new_posta = posta_entry.get()

                # Подключение к базе данных
                conn = sqlite3.connect("apteka.db")
                cursor = conn.cursor()

                # Обновление записи в таблице products
                try:
                    cursor.execute("UPDATE products SET name=?, price=?, quantity=?, packing=?, supplier=? WHERE id=?",
                                  (new_name, new_price, new_quantity, new_pacing, new_posta, product_id))
                    conn.commit()
                    print(f"Строка с ID {product_id} обновлена.")

                    # Обновление данных в Treeview
                    tree.item(selected_item[0], values=(new_name, new_price, new_quantity, new_pacing, new_posta,  product_id))

                    # Закрытие окна редактирования
                    edit_window.destroy()
                except Exception as e:
                    print(f"Ошибка при обновлении строки: {e}")

                # Закрытие соединения с базой данных
                conn.close()

            save_button = tk.Button(edit_window, text="Сохранить", command=save_changes)
            save_button.grid(row=7, column=0, columnspan=2, pady=10)



    # Подключение к базе данных
    conn = sqlite3.connect("apteka.db")
    cursor = conn.cursor()

    # Получение данных из таблицы products
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    # Создание фрейма для таблицы
    table_frame = tk.Frame(goods_window)
    table_frame.pack(pady=50)

    # Создание Treeview
    tree = ttk.Treeview(table_frame, columns=[column[0] for column in cursor.description], show="headings")
    tree.pack(side="left", fill="both", expand=True)

    # Заголовки столбцов
    for i, column in enumerate(cursor.description):
        tree.heading(column[0], text=column[0])
        tree.column(column[0], anchor="w", width=100, stretch=True)  # Выравнивание по левому краю

    # Данные таблицы
    for row in products:
        tree.insert("", "end", values=row)

    # Создание скроллбаров
    scrollbar_y = tk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
    scrollbar_y.pack(side="right", fill="y")
    scrollbar_x = tk.Scrollbar(table_frame, orient="horizontal", command=tree.xview)
    scrollbar_x.pack(side="bottom", fill="x")

    # Связывание скроллбаров с Treeview
    tree.config(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

    # Закрытие соединения с базой данных
    conn.close()

    # Поле поиска
    search_frame = tk.Frame(goods_window)
    search_frame.pack(pady=10)
    search_label = tk.Label(search_frame, text="Поиск:")
    search_label.pack(side="left")
    search_entry = tk.Entry(search_frame)
    search_entry.pack(side="left")
    search_entry.bind("<KeyRelease>", search_products)  # Вызов поиска при каждом изменении текста

    button_frame = tk.Frame(goods_window)
    button_frame.pack(pady=30)

    # Кнопка редактирования
    edit_button = tk.Button(button_frame, text="Редактировать", command=edit_selected_row, width=20, height=5)
    edit_button.pack(side="left", padx=10)

    delete_button = tk.Button(button_frame, text="Удалить", command=delete_selected_row, width=20, height=5)
    delete_button.pack(side="left", padx=10)
    
    total_cost_button = tk.Button(button_frame, text="Сумарная стоимость", command=calculate_total_cost, width=20, height=5)
    total_cost_button.pack(side="left", pady=50)

    back_button = tk.Button(button_frame, text="Назад", command=close_goods_window, width=20, height=5)
    back_button.pack(side="left", padx=10)

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("Главное окно")
root.geometry("500x500")

button_frame1 = tk.Frame(root)
button_frame1.pack(pady=50)

cabinet_button = tk.Button(button_frame1, text="Кабинет", command=open_cabinet_window, width=20, height=5)
cabinet_button.pack(side="left", padx=20)

goods_button = tk.Button(button_frame1, text="Товары", command=open_goods_window, width=20, height=5)
goods_button.pack(side="left", padx=20)

# Второй ряд кнопок
button_frame2 = tk.Frame(root)
button_frame2.pack(pady=50)

suppliers_button = tk.Button(button_frame2, text="Поставщики", command=open_cabinet_window, width=20, height=5)
suppliers_button.pack(side="left", padx=20)

exit_button = tk.Button(button_frame2, text="Выход", command=exit_app, width=20, height=5)
exit_button.pack(side="left", padx=20)

root.mainloop()