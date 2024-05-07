import customtkinter
from customtkinter import *

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()  # create CTk window like the Tk() constructor
app.geometry("400x200")
app.title("Apteka.BY")

correct_login = "user"
correct_password = "password"


def login_command():
    if entry_1.get() == correct_login and entry_2.get() == correct_password:
        new_window = customtkinter.CTk()
        new_window.geometry("200x100")
        new_window.title("Login Window")
    else:
        print("Incorrect login or password")


def register_command():
    new_window = customtkinter.CTk()
    new_window.geometry("200x100")
    new_window.title("Registration Window")

    def save_command():
        print("Save button clicked")

    button_3 = customtkinter.CTkButton(master=new_window, text="СОХРАНИТЬ", command=save_command)
    button_3.pack(pady=20)


frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=20)

label_1 = customtkinter.CTkLabel(master=frame_1, text="Login", width=120, height=25)
label_1.grid(row=0, column=0, columnspan=2)

entry_1 = customtkinter.CTkEntry(master=frame_1, width=200, height=25)
entry_1.grid(row=1, column=0, columnspan=2)

label_2 = customtkinter.CTkLabel(master=frame_1, text="Parol", width=120, height=25)
label_2.grid(row=2, column=0, columnspan=2)

entry_2 = customtkinter.CTkEntry(master=frame_1, width=200, height=25)
entry_2.grid(row=3, column=0, columnspan=2)

button_1 = customtkinter.CTkButton(master=frame_1, text="Vhod", command=login_command)
button_1.grid(row=4, column=0, pady=10, padx=10)

button_2 = customtkinter.CTkButton(master=frame_1, text="Registracia", command=register_command)
button_2.grid(row=4, column=1, pady=10, padx=10)

app.mainloop()