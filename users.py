from tkinter import *
from tkinter import ttk


def register_user():
    label_input_login = Label(text='Введите логин')
    label_input_login.place(x=20, y=90)
    user_login = ttk.Entry()
    user_login.place(x=20, y=120)
    label_input_password = Label(text='Введите пароль')
    label_input_password.place(x=20, y=150)
    user_password = ttk.Entry(show='*')
    user_password.place(x=20, y=180)
    label_input_password = Label(text='Введите пароль ещё раз')
    label_input_password.place(x=20, y=210)
    user_password2 = ttk.Entry(show='*')
    user_password2.place(x=20, y=240)

