from tkinter import *
from tkinter import ttk

from db import *


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
    btn_register = ttk.Button(text='Регистрация',
                              command=lambda: register_data(user_password.get(), user_password2.get(),user_login.get()))
    btn_register.place(x=20, y=280)


def register_data(user_password, user_password2, user_login): # Обёртка для lamda функции
    register(user_password, user_password2, user_login)

def register(user_password, user_password2, user_login):
    if user_password == user_password2 and len(user_password) > 6:
        c.execute('''CREATE TABLE IF NOT EXISTS users
                        (date datetime, nick char, password char, admin int) ''') # Проверяем есть ли база и если её нет - создаём
        conn.commit()
        c.execute("SELECT nick FROM users")
        arr_user_login = c.fetchall()
        if user_login in [item[0] for item in arr_user_login]:
            print('Имя занято')
        else:
            user_data = user_login, user_password
            c.execute('INSERT INTO users(nick, password) VALUES(?, ?)', user_data)
            conn.commit()
            print('Запись!')
    else:
        print('Пароль не может быть использован!')

