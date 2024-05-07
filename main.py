import customtkinter
from customtkinter import *
import subprocess

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-green"

correct_login = "user"
correct_password = "password"


def open_second_window():
    first_window.destroy()
    second_window = customtkinter.CTk()
    second_window.geometry("400x200")
    second_window.title("Second Window")
    second_window.mainloop()

    label = customtkinter.CTkLabel(master=second_window, text="Успех!", width=200, height=100)
    label.pack(pady=20)


def login_command():
    if entry_1.get() == correct_login and entry_2.get() == correct_password:
        open_second_window()
    else:
        print("Incorrect login or password")


first_window = customtkinter.CTk()
first_window.geometry("400x200")
first_window.title("Apteka.BY")

frame_1 = customtkinter.CTkFrame(master=first_window)
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

button_2 = customtkinter.CTkButton(master=frame_1, text="Registracia", command=open_second_window)
button_2.grid(row=4, column=1, pady=10, padx=10)

first_window.mainloop()