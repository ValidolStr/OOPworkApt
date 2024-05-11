import flet as ft
import sqlite3

def main (page: ft.Page):
    page.title = "Apteka.By"
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 700
    page.window_height = 500
    page.window_resizable = False
    
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
            btnauth.on_click = page.add(menu)
            page.navigation_bar = ft.NavigationBar(
            destinations=[
            ft.NavigationDestination(icon=ft.icons.STAR_HALF, label="Сотрудники"),
            ft.NavigationDestination(icon=ft.icons.MEDICAL_SERVICES, label="Аптека"),
            ft.NavigationDestination(icon=ft.icons.WAREHOUSE, label="Склад"),
            ft.NavigationDestination(icon=ft.icons.PEOPLE, label="Поставщики"),
            ft.NavigationDestination(icon=ft.icons.PENDING, label="Заказ"),
            ft.NavigationDestination(icon=ft.icons.HOME, label="Выход")
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
    btnadmin = ft.OutlinedButton(text='Админ', width=200, on_click=auth, disabled=True )  

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
    
    

    menu = ft.Row([
            ft.Column([
                ft.Text(f"Добро пожаловать"),
                

                    ]      
                )
        ],
        alignment=ft.MainAxisAlignment.CENTER     
    )
    
    def menunavigator (e):
        pass
    
    page.add(panel_autorise)  
     
ft.app(target=main)
    


