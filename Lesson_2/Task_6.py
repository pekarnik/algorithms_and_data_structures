# В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10
# попыток. После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то,
# что загадано. Если за 10 попыток число не отгадано, вывести ответ.

from random import randint
rand = randint(0, 100)
tries = 10
n = int(input('Введите число '))
tries -= 1
while n != rand:
    if n> rand:
        print('Больше')
    else:
        print('Меньше')
    n = int(input('Введите число '))
if tries > 0:
    print('Победа')
else:
    print(rand)