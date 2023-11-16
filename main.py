import sqlite3

conn = sqlite3.connect('MyTestBD.bd')

c = conn.cursor()
try:
    c.execute('''CREATE TABLE users
                (date datetime, nick char, password char, admin int) ''')
except:
    print("БД users уже создана! \n")
conn.commit()  # Сохранение изменений
answerUser: str = input("Зарегестрироваться(reg) или войти(login)?\n")
if answerUser == 'reg':
    loginUser: str = input('Login?: \n')
    passwordUser: str = input('Password?: \n')
    passwordUser2: str = input('Password again?: \n')
    if passwordUser == passwordUser2:
        c.execute('SELECT nick FROM users')
        allNick = c.fetchall()
        # for i in allNick:
        if loginUser in [item[0] for item in allNick]:
            print('Такое имя уже используется! \n')
        else:
            user = (loginUser, passwordUser)
            c.execute('INSERT INTO users (nick,password) VALUES(?, ?)', user)
            conn.commit()
            print('Запись успешно внесена в БД')
    else:
        print("Пароли не совпадают")
if answerUser == ('login'):
    userLogin = input('Введите login: \n')
    userPassword = input('Введите пароль: \n')
    c.execute('SELECT nick FROM users')
    allNick = c.fetchall()
    for i in allNick:
        if i[0] == userLogin:
            c.execute('SELECT password FROM users WHERE nick = ?', (userLogin,))
            stored_password = c.fetchone()
            if stored_password and str(stored_password[0]) == userPassword:
                print(f"Удачный вход! login: {i[0]} password: {stored_password[0]} \n")
                break
conn.close()  # разрыв связи с БД
