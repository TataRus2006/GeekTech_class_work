# Введение в Python: Встроенные функции, переменные, комментарии.
# Базовые типы данных: строки, целые и дробные числа
# Логический тип данных, условные конструкции и операторы.

# a, b = 3, 2
#
# print(a, b)
#
# a = 2
# b = 3

# print(type(True))
# print(bool())
# print(bool(1))
# print(bool(0.0))

# True, False
# and, or, not

a = 0
word = input('word: ')
a += len(word)
print(a)


# month = int(input('введите месяц рождения: '))
#
# if month == 1 or month == 2 or month == 12:
#     print('winter')
# elif 3 <= month <= 5:
#     print('spring')
# elif 6 <= month <= 8:
#     print('summer')
# elif 9 <= month <= 11:
#     print('autumn')
# else:
#     print("вводите числа только от 1 до 12 в формате 01 либо 1")

    # if not word.isalpha() and not word.isdigit() and len(word) >= 6:
    #     print('ok')
    # else:
    #     print('bad password!')

    # # [start:end:step]
    # print(word)
    # print(word[0])
    # print(word[::2])
    # new = word[3:6]
    # print(new, 'новый объект')
    # print(word[:2])

    # print(5 == 1+4)
    # print(5 != 1+3)
    #
    # print(1 < 5 and 5 < 6)
    # print(1 < 5 < 6)
    # print(type(2 > 1))
    # print(2 > 1)
    # print(2 >= 2)
    # print(2 > 2 or 2 == 2)
    # print(2 > 1 and 2 == 2)
    # print(2 != 2 or 2 != 3)
    # print(2 != 4 and 2 != 3)

    # signal = input('введите цвет: ')
    #
    # if signal == 'red' or signal == 'красный':
    #     print('stop')
    # elif signal == 'green' or signal == 'зеленый':
    #     print('go')
    # elif signal == 'yellow' or signal == 'желтый':
    #     print('готовимся')
    # else:
    #     print('смотрим по ситуации!')
    #     situation = input('Опишите ситуацию: ')
    #     if situation == 'off' or situation == 'отключен':
    #         print("смотрим на право!")
    #     elif situation == 'police':
    #         print('следуем команде инспектора')
