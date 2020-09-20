# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = int(input('Введите первое число\n'))
b = int(input('Введите второе число\n'))
c = int(input('Введите третье число\n'))
res = a
if a > b:
    if b > c:
        res = b
    else:
        if a > c:
            res = c
        else:
            res = a
else:
    if a > c:
        res = a
    else:
        if b > c:
            res = c
        else:
            res = b
print(f'Среднее число {res}')
