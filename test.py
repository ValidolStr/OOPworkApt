import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from datetime import datetime, timedelta

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
        "UNP": "490704065",
        "Юридический адрес": "г. Наровля ул. Ленина, д. 6",
        "Email": "apteka@example.com",
        "Телефон": "+375 123 456 789",
        "Название": "Аптека №101"
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

#ТОВАРЫ

def open_goods_window():
    global root
    root.withdraw()
    goods_window = tk.Toplevel(root)
    goods_window.title("Товары")
    goods_window.geometry("800x700")

    def close_goods_window():
        goods_window.destroy()
        root.deiconify()


    def add_supplier():
        # Получение данных из полей ввода
        new_name = name_entry.get()
        new_price = price_entry.get()
        new_pacing = pacing_entry.get()
        new_quantity = quantity_entry.get()
        new_posta = posta_entry.get()
        new_date = date_entry.get()
        
        # ... (получение других данных о поставщике)

        # Проверка введенных данных (необязательно, но рекомендуется)
        if not (new_name and new_price and new_pacing and new_quantity and new_posta and new_date):
            # Вывод сообщения об ошибке, если имя поставщика не введено
            tk.messagebox.showerror("Ошибка", "Введите все данные нового товара")
            return

        # Подключение к БД
        conn = sqlite3.connect("db_name")
        cursor = conn.cursor()

        # Вставка данных в БД
        try:
            cursor.execute(
                "INSERT INTO products (name, price, quantity, packing, postav_id, expirationdate) VALUES (?, ?, ?, ?, ?, ?)",
                (new_name, new_price, new_quantity, new_pacing, new_posta, new_date),
            )
            conn.commit()
            tk.messagebox.showinfo("Успешно", "Товавр добавлен")
        except Exception as e:
            tk.messagebox.showerror("Ошибка", f"Ошибка добавления товара: {e}")
        finally:
            conn.close()

        # Обновление списка поставщиков (необязательно, но рекомендуется)
        # ... (код для обновления списка поставщиков)


    def delete_selected_row():
        selected_item = tree.selection()
        if selected_item:
            # Получение ID выбранной строки
            product_id = tree.item(selected_item[0])['values'][0]  # Предполагается, что ID - первый столбец

            # Подключение к базе данных
            conn = sqlite3.connect("db_name")
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

    def check_expired_products():
        """Определяет товары с истекшим сроком годности на сегодняшнюю дату."""

        today = datetime.now().date()

        # Подключение к базе данных
        conn = sqlite3.connect("db_name")
        cursor = conn.cursor()

        # Запрос для получения товаров с истекшим сроком годности
        cursor.execute("""
            SELECT * FROM products
            WHERE strftime('%Y-%m-%d', ExpirationDate) < strftime('%Y-%m-%d', 'now')
        """)

        expired_products = cursor.fetchall()
        conn.close()

        # Создание нового окна для вывода информации
        expired_window = tk.Toplevel(root)  # root - это ваше главное окно
        expired_window.title("Товары с истекшим сроком годности")

        # Создание текстового виджета для вывода информации
        text_widget = tk.Text(expired_window, wrap=tk.WORD)
        text_widget.pack(expand=True, fill="both")

        # Вывод списка товаров с истекшим сроком годности
        if expired_products:
            text_widget.insert(tk.END, "Товары с истекшим сроком годности:\n")
            for product in expired_products:
                text_widget.insert(tk.END, f"  - {product[1]} (Срок годности: {product[5]})\n")
        else:
            text_widget.insert(tk.END, "Товаров с истекшим сроком годности нет.\n")

        # Делаем текстовый виджет нередактируемым
        text_widget.config(state=tk.DISABLED)


    def search_products(event=None):
        search_term = search_entry.get()
        if search_term:
            # Подключение к базе данных
            conn = sqlite3.connect("db_name")
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
            conn = sqlite3.connect("db_name")
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
        conn = sqlite3.connect("db_name")
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
            quantity_entry.insert(0, current_values[4])
            quantity_entry.grid(row=3, column=1, padx=5, pady=5)
            
            posta_label = tk.Label(edit_window, text="Поставщик:")
            posta_label.grid(row=4, column=0, padx=5, pady=5)
            posta_entry = tk.Entry(edit_window, width=50)
            posta_entry.insert(0, current_values[6])
            posta_entry.grid(row=4, column=1, padx=5, pady=5)
            
            srok_label = tk.Label(edit_window, text="Срок годности:")
            srok_label.grid(row=5, column=0, padx=5, pady=5)
            srok_entry = tk.Entry(edit_window, width=50)
            srok_entry.insert(0, current_values[5])
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
                conn = sqlite3.connect("db_name")
                cursor = conn.cursor()

                # Обновление записи в таблице products
                try:
                    cursor.execute("UPDATE products SET name=?, price=?, quantity=?, packing=?, postav_id=? WHERE id=?",
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
    conn = sqlite3.connect("db_name")
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


    column1_frame = tk.Frame(goods_window)
    column1_frame.pack(side="left", padx=20)

    name_label = tk.Label(column1_frame, text="Имя товара:")
    name_label.pack(pady=1)
    name_entry = tk.Entry(column1_frame)
    name_entry.pack(pady=1)

    price_label = tk.Label(column1_frame, text="Цена:")
    price_label.pack(pady=1)
    price_entry = tk.Entry(column1_frame)
    price_entry.pack(pady=1)

    pacing_label = tk.Label(column1_frame, text="Фасовка:")
    pacing_label.pack(pady=1)
    pacing_entry = tk.Entry(column1_frame)
    pacing_entry.pack(pady=1)

    quantity_label = tk.Label(column1_frame, text="Количество:")
    quantity_label.pack(pady=1)
    quantity_entry = tk.Entry(column1_frame)
    quantity_entry.pack(pady=1)

    posta_label = tk.Label(column1_frame, text="Поставщик:")
    posta_label.pack(pady=1)
    posta_entry = tk.Entry(column1_frame)
    posta_entry.pack(pady=1)

    date_label = tk.Label(column1_frame, text="Срок годности:")
    date_label.pack(pady=1)
    date_entry = tk.Entry(column1_frame)
    date_entry.pack(pady=1)

    # Второй столбец (кнопка "Добавить")
    column2_frame = tk.Frame(goods_window)
    column2_frame.pack(side="left", padx=20)

    add_button = tk.Button(column2_frame, text="Добавить", command=add_supplier, width=20, height=5)
    add_button.pack(pady=10)
    
    data_button = tk.Button(column2_frame, text="Проверка сроков", command=check_expired_products, width=20, height=5)
    data_button.pack(pady=10)

    # Третий столбец (остальные кнопки)
    column3_frame = tk.Frame(goods_window)
    column3_frame.pack(side="left", padx=20)

    # Первый ряд кнопок
    button_frame_top = tk.Frame(column3_frame)
    button_frame_top.pack(pady=10)

    edit_button = tk.Button(button_frame_top, text="Редактировать", command=edit_selected_row, width=20, height=5)
    edit_button.pack(side="left", padx=10)

    delete_button = tk.Button(button_frame_top, text="Удалить", command=delete_selected_row, width=20, height=5)
    delete_button.pack(side="left", padx=10)

    # Второй ряд кнопок
    button_frame_bottom = tk.Frame(column3_frame)
    button_frame_bottom.pack(pady=10)

    total_cost_button = tk.Button(button_frame_bottom, text="Сумарная стоимость", command=calculate_total_cost, width=20, height=5)
    total_cost_button.pack(side="left", padx=10)

    back_button = tk.Button(button_frame_bottom, text="Назад", command=close_goods_window, width=20, height=5)
    back_button.pack(side="left", padx=10)
    
#ТОВАРЫ
    
#___________________________________________________________________________________________
#Поставщик "БЕЛЛЕКФАРМ"


def open_BELLECFARM_window():
    global root
    root.withdraw()
    open_BELLECFARM_window = tk.Toplevel(root)
    open_BELLECFARM_window .title("Бел Лек Гроуп")
    open_BELLECFARM_window .geometry("800x700")

    def close_supp_windowsup():
        open_BELLECFARM_window.destroy()
        open_suppliers_window.deiconify()

    def delete_selected_rowsup():
        selected_item = tree.selection()
        if selected_item:
            # Получение ID выбранной строки
            suppilbellec_id = tree.item(selected_item[0])['values'][0]  # Предполагается, что ID - первый столбец

            # Подключение к базе данных
            conn = sqlite3.connect("db_name")
            cursor = conn.cursor()

            # Удаление записи из таблицы products
            try:
                cursor.execute("DELETE FROM suppilbellec WHERE id=?", (suppilbellec_id,))
                conn.commit()
                tree.delete(selected_item)  # Удаление строки из Treeview
                print(f"Строка с ID {suppilbellec_id} удалена из таблицы products.")
            except Exception as e:
                print(f"Ошибка при удалении строки: {e}")

            # Закрытие соединения с базой данных
            conn.close()

    def search_products(event=None):
        search_term = search_entry.get()
        if search_term:
            # Подключение к базе данных
            conn = sqlite3.connect("db_name")
            cursor = conn.cursor()

            # Поиск в базе данных
            cursor.execute("SELECT * FROM suppilbellec WHERE name LIKE ?", ('%' + search_term + '%',))
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
            conn = sqlite3.connect("db_name")
            cursor = conn.cursor()

            # Получение всех товаров
            cursor.execute("SELECT * FROM suppilbellec")
            products = cursor.fetchall()

            # Добавление всех товаров в Treeview
            for row in products:
                tree.insert("", "end", values=row)

            # Закрытие соединения с базой данных
            conn.close()

    def edit_selected_rowsup():
        selected_item = tree.selection()
        if selected_item:
            # Получение ID выбранной строки
            suppilbellec_id = tree.item(selected_item[0])['values'][0]

            # Получение текущих значений строки
            current_values = tree.item(selected_item[0])['values']

            # Создание окна редактирования
            edit_window = tk.Toplevel(open_BELLECFARM_window )
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
            quantity_entry.insert(0, current_values[4])
            quantity_entry.grid(row=3, column=1, padx=5, pady=5)
            
            
            srok_label = tk.Label(edit_window, text="Срок годности:")
            srok_label.grid(row=5, column=0, padx=5, pady=5)
            srok_entry = tk.Entry(edit_window, width=50)
            srok_entry.insert(0, current_values[5])
            srok_entry.grid(row=5, column=1, padx=5, pady=5)

            # Кнопка сохранения изменений
            def save_changes():
                # Получение новых значений из полей ввода
                new_name = name_entry.get()
                new_price = price_entry.get()
                new_pacing = pacing_entry.get()
                new_quantity = quantity_entry.get()

                # Подключение к базе данных
                conn = sqlite3.connect("db_name")
                cursor = conn.cursor()

                # Обновление записи в таблице products
                try:
                    cursor.execute("UPDATE suppilbellec SET name=?, price=?, quantity=?, packing=? WHERE id=?",
                                  (new_name, new_price, new_quantity, new_pacing, suppilbellec_id))
                    conn.commit()
                    print(f"Строка с ID {suppilbellec_id} обновлена.")

                    # Обновление данных в Treeview
                    tree.item(selected_item[0], values=(new_name, new_price, new_quantity, new_pacing, suppilbellec_id))

                    # Закрытие окна редактирования
                    edit_window.destroy()
                except Exception as e:
                    print(f"Ошибка при обновлении строки: {e}")

                # Закрытие соединения с базой данных
                conn.close()

            save_button = tk.Button(edit_window, text="Сохранить", command=save_changes)
            save_button.grid(row=7, column=0, columnspan=2, pady=10)



    # Подключение к базе данных
    conn = sqlite3.connect("db_name")
    cursor = conn.cursor()

    # Получение данных из таблицы products
    cursor.execute("SELECT * FROM suppilbellec")
    products = cursor.fetchall()

    # Создание фрейма для таблицы
    table_frame = tk.Frame(open_BELLECFARM_window)
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
    search_frame = tk.Frame(open_BELLECFARM_window )
    search_frame.pack(pady=10)
    search_label = tk.Label(search_frame, text="Поиск:")
    search_label.pack(side="left")
    search_entry = tk.Entry(search_frame)
    search_entry.pack(side="left")
    search_entry.bind("<KeyRelease>", search_products)  # Вызов поиска при каждом изменении текста

    button_frame = tk.Frame(open_BELLECFARM_window)
    button_frame.pack(pady=30)

    # Кнопка редактирования
    edit_button = tk.Button(button_frame, text="Редактировать", command=edit_selected_rowsup, width=20, height=5)
    edit_button.pack(side="left", padx=10)

    delete_button = tk.Button(button_frame, text="Удалить", command=delete_selected_rowsup, width=20, height=5)
    delete_button.pack(side="left", padx=10)

    back_button = tk.Button(button_frame, text="Назад", command=close_supp_windowsup, width=20, height=5)
    back_button.pack(side="left", padx=10)

#___________________________________________________________________________________________
#Поставщик "БЕЛЛЕКФАРМ"

#___________________________________________________________________________________________
#Поставщик "Лекфарм"


def open_LECFARM_window():
    global root
    root.withdraw()
    open_LECFARM_window = tk.Toplevel(root)
    open_LECFARM_window .title("Лек Фарм")
    open_LECFARM_window .geometry("800x700")

    def close_supp_windowsup():
        open_LECFARM_window.destroy()
        open_suppliers_window.deiconify()

    def delete_selected_rowsup():
        selected_item = tree.selection()
        if selected_item:
            # Получение ID выбранной строки
            suppillec_id = tree.item(selected_item[0])['values'][0]  # Предполагается, что ID - первый столбец

            # Подключение к базе данных
            conn = sqlite3.connect("db_name")
            cursor = conn.cursor()

            # Удаление записи из таблицы products
            try:
                cursor.execute("DELETE FROM suppillecfarm WHERE id=?", (suppillec_id,))
                conn.commit()
                tree.delete(selected_item)  # Удаление строки из Treeview
                print(f"Строка с ID {suppillec_id} удалена из таблицы products.")
            except Exception as e:
                print(f"Ошибка при удалении строки: {e}")

            # Закрытие соединения с базой данных
            conn.close()

    def search_products(event=None):
        search_term = search_entry.get()
        if search_term:
            # Подключение к базе данных
            conn = sqlite3.connect("db_name")
            cursor = conn.cursor()

            # Поиск в базе данных
            cursor.execute("SELECT * FROM suppillecfarm WHERE name LIKE ?", ('%' + search_term + '%',))
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
            conn = sqlite3.connect("db_name")
            cursor = conn.cursor()

            # Получение всех товаров
            cursor.execute("SELECT * FROM suppillecfarm")
            products = cursor.fetchall()

            # Добавление всех товаров в Treeview
            for row in products:
                tree.insert("", "end", values=row)

            # Закрытие соединения с базой данных
            conn.close()

    def edit_selected_rowsuplec():
        selected_item = tree.selection()
        if selected_item:
            # Получение ID выбранной строки
            suppillec_id = tree.item(selected_item[0])['values'][0]

            # Получение текущих значений строки
            current_values = tree.item(selected_item[0])['values']

            # Создание окна редактирования
            edit_window = tk.Toplevel(open_LECFARM_window)
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
            quantity_entry.insert(0, current_values[4])
            quantity_entry.grid(row=3, column=1, padx=5, pady=5)
            
            
            srok_label = tk.Label(edit_window, text="Срок годности:")
            srok_label.grid(row=5, column=0, padx=5, pady=5)
            srok_entry = tk.Entry(edit_window, width=50)
            srok_entry.insert(0, current_values[5])
            srok_entry.grid(row=5, column=1, padx=5, pady=5)

            # Кнопка сохранения изменений
            def save_changes():
                # Получение новых значений из полей ввода
                new_name = name_entry.get()
                new_price = price_entry.get()
                new_pacing = pacing_entry.get()
                new_quantity = quantity_entry.get()

                # Подключение к базе данных
                conn = sqlite3.connect("db_name")
                cursor = conn.cursor()

                # Обновление записи в таблице products
                try:
                    cursor.execute("UPDATE suppillecfarm SET name=?, price=?, quantity=?, packing=? WHERE id=?",
                                  (new_name, new_price, new_quantity, new_pacing, suppillec_id))
                    conn.commit()
                    print(f"Строка с ID {suppillec_id} обновлена.")

                    # Обновление данных в Treeview
                    tree.item(selected_item[0], values=(new_name, new_price, new_quantity, new_pacing, suppillec_id))

                    # Закрытие окна редактирования
                    edit_window.destroy()
                except Exception as e:
                    print(f"Ошибка при обновлении строки: {e}")

                # Закрытие соединения с базой данных
                conn.close()

            save_button = tk.Button(edit_window, text="Сохранить", command=save_changes)
            save_button.grid(row=7, column=0, columnspan=2, pady=10)



    # Подключение к базе данных
    conn = sqlite3.connect("db_name")
    cursor = conn.cursor()

    # Получение данных из таблицы products
    cursor.execute("SELECT * FROM suppillecfarm")
    products = cursor.fetchall()

    # Создание фрейма для таблицы
    table_frame = tk.Frame(open_LECFARM_window)
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
    search_frame = tk.Frame(open_LECFARM_window )
    search_frame.pack(pady=10)
    search_label = tk.Label(search_frame, text="Поиск:")
    search_label.pack(side="left")
    search_entry = tk.Entry(search_frame)
    search_entry.pack(side="left")
    search_entry.bind("<KeyRelease>", search_products)  # Вызов поиска при каждом изменении текста

    button_frame = tk.Frame(open_LECFARM_window)
    button_frame.pack(pady=30)

    # Кнопка редактирования
    edit_button = tk.Button(button_frame, text="Редактировать", command=edit_selected_rowsuplec, width=20, height=5)
    edit_button.pack(side="left", padx=10)

    delete_button = tk.Button(button_frame, text="Удалить", command=delete_selected_rowsup, width=20, height=5)
    delete_button.pack(side="left", padx=10)

    back_button = tk.Button(button_frame, text="Назад", command=close_supp_windowsup, width=20, height=5)
    back_button.pack(side="left", padx=10)

#___________________________________________________________________________________________
#Поставщик "Лекфарм"



def open_suppliers_window():
    global root
    root.withdraw()
    suppliers_window = tk.Toplevel(root)
    suppliers_window.title("Поставщики")
    suppliers_window.geometry("800x700")

    def close_suppliers_window():
        suppliers_window.destroy()
        root.deiconify()

    # Кнопки для каждого поставщика
    button_framesup = tk.Frame(suppliers_window)
    button_framesup.pack(pady=20)  # Используйте pady только для button_framesup

    # Кнопки для поставщиков
    bell_group_button = tk.Button(button_framesup, text="БелЛекГроуп", command=open_BELLECFARM_window, width=20, height=5)
    bell_group_button.pack(side=tk.LEFT, padx=20)  # Расположите кнопку слева

    lekfarm_button = tk.Button(button_framesup, text="ЛекФарм", command=open_LECFARM_window, width=20, height=5)
    lekfarm_button.pack(side=tk.LEFT, padx=20)
    
    bell_group_button = tk.Button(button_framesup, text="ФармЛенд", command=open_FARM_window, width=20, height=5)
    bell_group_button.pack(side=tk.LEFT, padx=20)
    # ... (остальные кнопки)

    # Кнопка "Назад"
    back_button1 = tk.Button(suppliers_window, text="Назад", command=close_suppliers_window, width=20, height=5)
    back_button1.pack(pady=20)


#___________________________________________________________________________________________
#Поставщик "Фамленд"

def open_FARM_window():
    global root
    root.withdraw()
    open_FARM_window = tk.Toplevel(root)
    open_FARM_window .title("ФармЛенд")
    open_FARM_window .geometry("800x700")

    def close_supp_windowsup():
        open_FARM_window.destroy()
        open_suppliers_window.deiconify()

    def delete_selected_rowsup():
        selected_item = tree.selection()
        if selected_item:
            # Получение ID выбранной строки
            suppillec_id = tree.item(selected_item[0])['values'][0]  # Предполагается, что ID - первый столбец

            # Подключение к базе данных
            conn = sqlite3.connect("db_name")
            cursor = conn.cursor()

            # Удаление записи из таблицы products
            try:
                cursor.execute("DELETE FROM suppilfarm WHERE id=?", (suppillec_id,))
                conn.commit()
                tree.delete(selected_item)  # Удаление строки из Treeview
                print(f"Строка с ID {suppillec_id} удалена из таблицы products.")
            except Exception as e:
                print(f"Ошибка при удалении строки: {e}")

            # Закрытие соединения с базой данных
            conn.close()

    def search_products(event=None):
        search_term = search_entry.get()
        if search_term:
            # Подключение к базе данных
            conn = sqlite3.connect("db_name")
            cursor = conn.cursor()

            # Поиск в базе данных
            cursor.execute("SELECT * FROM suppilfarm WHERE name LIKE ?", ('%' + search_term + '%',))
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
            conn = sqlite3.connect("db_name")
            cursor = conn.cursor()

            # Получение всех товаров
            cursor.execute("SELECT * FROM suppilfarm")
            products = cursor.fetchall()

            # Добавление всех товаров в Treeview
            for row in products:
                tree.insert("", "end", values=row)

            # Закрытие соединения с базой данных
            conn.close()

    def edit_selected_rowsuplec():
        selected_item = tree.selection()
        if selected_item:
            # Получение ID выбранной строки
            suppillec_id = tree.item(selected_item[0])['values'][0]

            # Получение текущих значений строки
            current_values = tree.item(selected_item[0])['values']

            # Создание окна редактирования
            edit_window = tk.Toplevel(open_FARM_window)
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
            quantity_entry.insert(0, current_values[4])
            quantity_entry.grid(row=3, column=1, padx=5, pady=5)
            
            
            srok_label = tk.Label(edit_window, text="Срок годности:")
            srok_label.grid(row=5, column=0, padx=5, pady=5)
            srok_entry = tk.Entry(edit_window, width=50)
            srok_entry.insert(0, current_values[5])
            srok_entry.grid(row=5, column=1, padx=5, pady=5)

            # Кнопка сохранения изменений
            def save_changes():
                # Получение новых значений из полей ввода
                new_name = name_entry.get()
                new_price = price_entry.get()
                new_pacing = pacing_entry.get()
                new_quantity = quantity_entry.get()

                # Подключение к базе данных
                conn = sqlite3.connect("db_name")
                cursor = conn.cursor()

                # Обновление записи в таблице products
                try:
                    cursor.execute("UPDATE suppilfarm SET name=?, price=?, quantity=?, packing=? WHERE id=?",
                                  (new_name, new_price, new_quantity, new_pacing, suppillec_id))
                    conn.commit()
                    print(f"Строка с ID {suppillec_id} обновлена.")

                    # Обновление данных в Treeview
                    tree.item(selected_item[0], values=(new_name, new_price, new_quantity, new_pacing, suppillec_id))

                    # Закрытие окна редактирования
                    edit_window.destroy()
                except Exception as e:
                    print(f"Ошибка при обновлении строки: {e}")

                # Закрытие соединения с базой данных
                conn.close()

            save_button = tk.Button(edit_window, text="Сохранить", command=save_changes)
            save_button.grid(row=7, column=0, columnspan=2, pady=10)



    # Подключение к базе данных
    conn = sqlite3.connect("db_name")
    cursor = conn.cursor()

    # Получение данных из таблицы products
    cursor.execute("SELECT * FROM suppilfarm")
    products = cursor.fetchall()

    # Создание фрейма для таблицы
    table_frame = tk.Frame(open_FARM_window)
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
    search_frame = tk.Frame(open_FARM_window )
    search_frame.pack(pady=10)
    search_label = tk.Label(search_frame, text="Поиск:")
    search_label.pack(side="left")
    search_entry = tk.Entry(search_frame)
    search_entry.pack(side="left")
    search_entry.bind("<KeyRelease>", search_products)  # Вызов поиска при каждом изменении текста

    button_frame = tk.Frame(open_FARM_window)
    button_frame.pack(pady=30)

    # Кнопка редактирования
    edit_button = tk.Button(button_frame, text="Редактировать", command=edit_selected_rowsuplec, width=20, height=5)
    edit_button.pack(side="left", padx=10)

    delete_button = tk.Button(button_frame, text="Удалить", command=delete_selected_rowsup, width=20, height=5)
    delete_button.pack(side="left", padx=10)

    back_button = tk.Button(button_frame, text="Назад", command=close_supp_windowsup, width=20, height=5)
    back_button.pack(side="left", padx=10)

#___________________________________________________________________________________________
#Поставщик "Фармленд"


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

suppliers_button = tk.Button(button_frame2, text="Поставщики", command=open_suppliers_window, width=20, height=5)
suppliers_button.pack(side="left", padx=20)

exit_button = tk.Button(button_frame2, text="Выход", command=exit_app, width=20, height=5)
exit_button.pack(side="left", padx=20)

root.mainloop()