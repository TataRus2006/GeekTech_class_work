# Операторы, булеаны, условные конструкции, циклы For, While
# Логический тип данных, условные конструкции и операторы.

# # or, and, not

# операторы сравнения
# print(2==2)             # равенство
# print(5-2 == 2+1)
# print(2 !=2)            # не равенство: - not
# print()
# print(2 > 2)            # больше
# print(2 >= 2)           # больше или равно
# print(2 > 2 or 2 == 2)  # or работает в случае "или", один из вариантов должен быть верным, тогда true, иначе false
# print(2 < 2)            # меньше
# print(2 <= 2)           # меньше или равно
# print(2 > 1 and 3 >1)   # and работает в случае "и", оба варианта должны быть верны, тогда true, иначе false
# print(2 > 1 < 3)

if 5 > 1:
    print('>')
elif 5 < 1:
    print('<')



# Пример: Светофор

# signal = input("введите цвет: ")
#
# if signal == 'red' or signal == 'красный':
#     print('stop')
# elif signal == 'green' or signal == 'зеленый':
#     print('go')
# elif signal == 'yellow' or signal == 'желтый':
#     print('готовимся')
# else:
#     print('смотрим по ситуации!')
#     situation = input('опишите ситуацию:')
#     if situation == 'off' or situation == 'отключен':
#         print('смотрим на право!')
#     elif situation == 'police':
#         print('следуем команде инспектора')
#     else:
#         print('позвоните в 911, \n'
#               'ждите, помощь в пути!')
#
# sum_of_ages = 14 + 16 + 18 + 26 + 11 + 14 + 31 + 13 + 19 + 16 + 21 + 20 + 16 + 41 + \
#               + 32 + 34 + 18 + 28