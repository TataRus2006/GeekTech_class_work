# for, while

# circle = 0
#
# while circle != 10:
#     circle += 1
#     print(f'пробежали {circle} кругов!')
#     if circle == 5:
#         print('перекур!')
#         continue
#     elif circle == 8:
#         print('на сегодня все')
#         break

i = 0
new = ''
while True:
    start = input('Да или нет?')
    if start.lower() == 'да':
        numbers = '123456789'
        user = input('введите число для выхода: ')
        if user == numbers[i]:
            new += numbers[i]
            print(new)
            i += 1
        else:
            print('повторите заново')
    elif start.lower() == 'нет':
        print('good buy!')
        break
    else:
        print("неверный ввод")


    # for i in numbers:
    #     print(i)
    #     user = input('введите число: ')
    #     if user != i:
    #         print('неправильно!')
    #         continue
    #     else:
    #         new += i
    #         print(new)



# rus_alpha = 'йцукенгшщзхъфывапролджэячсмитьбю'
# eng_alpha = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
#
# word = 'йцукенgbhfn'
#
# for i in word:
#     print(i, end=' ')
#
# print(word.index('f'))
# print(eng_alpha[rus_alpha.index('у')])
#
#
# for i in word:
#     if i in rus_alpha:
#         print(eng_alpha[rus_alpha.index(i)], end='')
#     else:
#         print(rus_alpha[eng_alpha.index(i)], end='')



# for i in range(1, 11):
#     if i == 8:
#         break
#     if i % 2 == 0:
#         print(i, "четное")
#     else:
#         print(i, "нечетное")
#
#     if i == 2:
#         print(i**2)
#     if i == 7:
#         print(i, 'мое число')
#     else:
#         print(i, 'остальные числа')


# star = 'python'
#
# word = 'p1ytrhosfn'
# # iterable
# c = 0
# for letter in word:
#     if letter in star:
#         print(letter)
#     else:
#         print(f' {letter} не находится в star')

    # if letter == 'r':
    #     print('конец цикла!')
    #     break
        # continue
    # c += 1
    # print(letter, c)

