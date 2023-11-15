from tkinter import *
from tkinter import ttk
from users import register_user


def start():
    btn_sign = ttk.Button(text='Вход')
    btn_sign.place(x=20, y=30)

    btn_reg = ttk.Button(text='Регистрация', command=register_user)
    btn_reg.place(x=120, y=30)


root = Tk()  # создаем корневой объект - окно
root.title("Приложение на Tkinter")  # устанавливаем заголовок окна
root.geometry("700x700")  # устанавливаем размеры окна

start()

root.mainloop()
