def get_string(txt):
    lst = txt.replace(',', '').replace('.', '').replace('(', '').\
        replace(')', '').replace('-', '').split(' ')
    line = ''
    for i in lst:
        if len(i) < 5:
            line += ' '+str(i)
    return line.strip()

s = """Было просто пасмурно, дуло с севера
А к обеду насчитал сто градаций серого.
Так всегда первого ноль девятого
То ли весь мир сошёл с ума, то ли я того
На столе записка от неё смятая
Недопитый виски допиваю с матами.
Посмотрю в окно, допишу главу
Первое сентября, дворник жжёт листву.
Серым облакам наплевать на нас
Если знаешь как жить - живи
Ты хотела плыть как все - так плыви
"""

t = get_string(s)
print(t)