import flet as ft
from flet import *
import sqlite3

def fetch_data_from_database():
    # Установка соединения с базой данных SQLite
    conn = sqlite3.connect('apteka.db')
    cursor = conn.cursor()

    # Выполнение SQL-запроса для извлечения данных из таблицы
    cursor.execute('SELECT * FROM users')
    data = cursor.fetchall()

    # Закрытие соединения с базой данных
    cursor.close()
    conn.close()

    return data

def main (page: ft.Page):
    page.title = "Apteka.By"
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 800
    page.window_height = 500
    page.window_resizable = False
    #page.scroll = "auto"
    
    def regisr (e):
        db = sqlite3.connect('apteka.db')
        cr = db.cursor()
        cr.execute("""CREATE TABLE IF NOT EXISTS users(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       login TEXT,
                       password TEXT
                       )""")
        cr.execute(f"INSERT INTO users VALUES(null, '{userlog.value}', '{userpass.value}')")
        db.commit()
        db.close()
        
        userlog.value = ''
        userpass.value = ''
        btnreg.text = 'Добавлено'
        page.update()


    def valid (e):
        if all([userlog.value, userpass.value]):
         btnreg.disabled = False
         btnauth.disabled = False
        else:
         btnreg.disabled = True
         btnreg.disabled= True
        
        page.update()
        
        
    def auth (e):
        db = sqlite3.connect('apteka.db')
        cr = db.cursor()
        
        cr.execute(f"SELECT * FROM users WHERE login = '{userlog.value}'AND password = '{userpass.value}'")
        if cr.fetchone() != None:
            page.clean()
            page.navigation_bar.destinations=None
            btnauth.on_click = page.add(panel_hallo)
            page.navigation_bar = ft.NavigationBar(
            destinations=[
            ft.NavigationDestination(icon=ft.icons.STAR_HALF, label="Сотрудники"),
            ft.NavigationDestination(icon=ft.icons.MEDICAL_SERVICES, label="Аптека"),
            ft.NavigationDestination(icon=ft.icons.WAREHOUSE, label="Склад"),
            ft.NavigationDestination(icon=ft.icons.PEOPLE, label="Поставщики"),
            ft.NavigationDestination(icon=ft.icons.PENDING, label="Заказ"),
        ], on_change=menunavigator
    )
            page.update()
        else:
            page.snack_bar = ft.SnackBar(ft.Text('Неверные данные!'))
            page.snack_bar.open = True
            userlog.value = ''
            userpass.value = ''
            page.update()
            
        
        db.commit()
        db.close()
    
    userlog = ft.TextField(label='Логин', on_change=valid)
    userpass = ft.TextField(label='Пароль', password=True, on_change=valid)
    btnreg = ft.OutlinedButton(text='Добавить', width=200, on_click=regisr, disabled=True )   
    btnauth = ft.OutlinedButton(text='Вход', width=200, on_click=auth, disabled=True )   
    

    panel_hallo = ft.Row([
                ft.Column([
                    ft.Text("Добро пожаловать"),
                   ]      
                    )
            ],
            alignment=ft.MainAxisAlignment.CENTER  
                
        )

    panel_reg = ft.Row([
            ft.Column([
                ft.Text("Регистрация"),
                userlog,
                userpass,
                btnreg     ]      
                )
        ],
        alignment=ft.MainAxisAlignment.CENTER  
            
    )
    
    panel_autorise = ft.Row([
            ft.Column([
                ft.Text("Авторизация"),
                userlog,
                userpass,
                btnauth     ]      
                )
        ],
        alignment=ft.MainAxisAlignment.CENTER  
            
    )
    
    def navigator (e):
        i = page.navigation_bar.selected_index
        page.clean()
        
        if i == 0:  page.add(panel_reg)
        elif i ==1: page.add(panel_autorise)
            
    
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.VERIFIED_USER, label="Регистрация"),
            ft.NavigationDestination(icon=ft.icons.VERIFIED_USER_OUTLINED, label="Авторизация")
        ], on_change=navigator
    )
    
    def menunavigator (e):
        i = page.navigation_bar.selected_index
        page.clean()
        
        if i == 0:                 
            page.add(personal_page),
            table.update()
        elif i ==1: 
            page.add(apteka_page)
        elif i ==2:
            page.add(sklad_page)
        elif i ==3: 
            page.add(postaw_page)
        elif i ==4: 
            page.add(zakaz_page)
  
    
    conn = sqlite3.connect('apteka.db')
    cursor = conn.cursor()

    # Получение данных из таблицы
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()

    # Создание заголовков колонок
    columns = [ft.DataColumn(ft.Text(header[0])) for header in cursor.description]
    columns.append(ft.DataColumn(ft.Text("Удаление")))
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

          
    text_field_1 = ft.TextField(label="Логин", read_only=True, width=150) 
    text_field_2 = ft.TextField(label="Пароль", read_only=True, width=150)
    new_value_1 = text_field_1.value
    new_value_2 = text_field_2.value
    
    selected_row_id = None
    def выбрать_ячейку(e, row_id):

        global selected_row_id
        selected_row_id = row_id
        # Получение значения из выбранной строки
        row_data = data[row_id-1]

        # Запись данных в текстовые поля
        text_field_1.value = str(row_data[1])  # Предполагаем, что первый столбец - column1
        text_field_2.value = str(row_data[2])  # Предполагаем, что второй столбец - column2
        text_field_1.read_only = False    
        text_field_2.read_only = False 
        # Обновление текстовых полей
        text_field_1.update()
        text_field_2.update()
    
    def update(e):
        global selected_row_id
        if selected_row_id is not None:
        # Получение новых значений из текстовых полей
            new_value_1 = text_field_1.value
            new_value_2 = text_field_2.value

        # Обновление данных в базе данных
        cursor.execute("UPDATE users SET login = ?, password = ? WHERE id = ?", (new_value_1, new_value_2, selected_row_id-1))
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
            
    personal_page = ft.Row([
    ft.Column([
        table,  # Ваша таблица
    ], scroll='always', width=400, height=300),  # Добавляем скроллинг к колонке с таблицей
    ft.Column([
        text_field_1,
        text_field_2, 
        ft.ElevatedButton(text="Обновить", on_click=update)
    ],)
    ],
    alignment=ft.MainAxisAlignment.CENTER,
    
    )
    
  
    apteka_page = ft.Row([
            ft.Column([
                ft.Text(f"Аптека"),
                

                    ]      
                )
        ],
        alignment=ft.MainAxisAlignment.CENTER     
    )
         
    
    
    sklad_page = ft.Row([
            ft.Column([
                ft.Text(f"Склад"),
                

                    ]      
                )
        ],
        alignment=ft.MainAxisAlignment.CENTER     
    )
       
    
    postaw_page = ft.Row([
            ft.Column([
                ft.Text(f"Поставки"),
                

                    ]      
                )
        ],
        alignment=ft.MainAxisAlignment.CENTER     
    )
        
        
    zakaz_page = ft.Row([
            ft.Column([
                ft.Text(f"Заказ"),
                

                    ]      
                )
        ],
        alignment=ft.MainAxisAlignment.CENTER     
    )
        
    
    
    page.add(panel_autorise)  
     
ft.app(target=main)
    


