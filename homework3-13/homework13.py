import json

def login_function(login, passwd):
    with open('reg.json', 'r') as f:
        reglist = json.load(f)
    if login in reglist.keys():
        if reglist[login] == passwd:
            print('Доступ разрешен!')
        else:
            print('Неверный пароль!')
    else:
        print('Неверный логин!')


