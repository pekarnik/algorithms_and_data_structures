# Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ
# от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f'
# включительно.

from random import randint, uniform

rand_int_min = int(input('Введите минимальное целое число\n'))
rand_int_max = int(input('Введите максимальное целое число\n'))
rand_real_min = float(input('Введите минимальное действительное число\n'))
rand_real_max = float(input('Введите максимальное действительное число\n'))
rand_symbol_min = input('Введите первый символ\n')
rand_symbol_max = input('Введите второй символ\n')
rand_int = randint(rand_int_min, rand_int_max)
rand_real = uniform(rand_real_min, rand_real_max)
rand_symbol = chr(randint(ord(rand_symbol_min), ord(rand_symbol_max)))
print(f'Случайное целое число {rand_int}')
print(f'Случайное вещественное число {rand_real}')
print(f'Случайный символ в промежутке {rand_symbol}')
