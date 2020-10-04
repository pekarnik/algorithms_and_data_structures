# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

symbol_1 = input('Введите первую букву\n').lower()
symbol_2 = input('Введите вторую букву\n').lower()
ord_symbol_1 = ord(symbol_1) - 96
ord_symbol_2 = ord(symbol_2) - 96
range_symbols = abs(ord_symbol_2 - ord_symbol_1)
print(f'Порядок первой буквы алфавита {ord_symbol_1}')
print(f'Порядок первой буквы алфавита {ord_symbol_2}')
print(f'Порядок первой буквы алфавита {range_symbols}')
