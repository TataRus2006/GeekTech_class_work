# lambda, exceptions
# lambda arguments: expression
# numbers = [i for i in range(1, 11)]
# print(numbers['asd'])
from random import choice

students = [1, 10, 5, 7, 6, 9]
materials = [1, 2, 3, 4, 5, 6, 7]
data = []

while len(students) != 0:
    print(students)
    student_id = choice(students)
    name = input(f'Имя студента под номером {student_id}: ')
    print(f"{name} отвечает на тему {choice(materials)}")
    while True:
        try:
            rate = int(input(f'Оценка для {name} '))
            if 0 < rate < 6:
                students.remove(student_id)
                data.append({name: rate})
                break
            else:
                print('от 1 до 5')
        except:
            print('Вводите только числа!')


for i in data:
    print(i)

# try:
#     print(10 / 0)
# except:
#     print('НЕ делим на ноль!')
#
# try:
#     name = 'samat'
#     print(nam)
# except:
#     print("неправильная переменная!")


# print(1 + '1'mbers = [i for i in range(1, 11)]
# print(numbers)
#
# new = list(map(lambda a: a * 2, numbers))
# print(new)
# print([i * 2 for i in numbers])
#
#
# filt = list(filter(lambda x: x > 6, numbers))
# print(filt)
# print([i for i in numbers if i > 6])

# a = lambda x: x + 5
# print(a(4))
#
#
# def b(x):
#     return x + 5
# print(b(4))
#
#
# words = ['python', 'geektech', 'exceptions', 'lambda']
# names = ['sam', 'tim', 'ken']
#
# def up_word(word):
#     return word.upper()
#
#
# def up_list(lst, func):
#     for i in lst:
#         print(func(i))
#
# up_list(words, up_word)
# up_list(words, lambda word: word.title())
# up_list(names, lambda word: word.upper())

