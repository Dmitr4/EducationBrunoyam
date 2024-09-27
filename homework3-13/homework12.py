import json

# r = {}
# with open('reg.json', 'a') as f:
#     json.dump(r, f)


def register(login, passwd):
    with open('reg.json', 'r') as f:
        reglist = json.load(f)

    if login not in reglist.keys():
        reglist[login] = passwd
        with open('reg.json', 'w') as f:
            json.dump(reglist, f)
    else:
        print('Пользователь с таким логином уже существует!')


register('anna', 'qwerty')


