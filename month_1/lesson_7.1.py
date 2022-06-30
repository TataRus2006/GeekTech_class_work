# lambda, и работа с исключениями
# lambda arguments: expression
# from random import choice
#
# students = [2, 3, 5, 6, 7, 9, 10, 12, 13, 15]
#
# data = []
#
# while len(students) != 0:
#     print(students)
#     student_id = choice(students)
#     name = input(f'Введите имя студента {student_id}: ').title()
#     try:
#         rate = int(input(f'Оценка для {name}: '))
#     except:
#         print('Введите число!')
#         continue
#     students.remove(student_id)
#     data.append({name: rate})
#
# for i in data:
#     print(i)


# try:
#     print(10 / 0)
# except:
#     print('Не делим на ноль!')
#
# try:
#     name = 'aza'
#     print(name)
# except:
#     print("нет такой переменной")
# finally:
#     print('конец!')

# numbers = list(range(1, 11))
# print(numbers)
# #
# new = list(filter(lambda x: x % 0, numbers))
# print(new)
# print([i for i in numbers if i < 5])
#
# new = list(map(lambda x: x * x, numbers))
# print(new)
# print([i*i for i in numbers])

# movies = {
#     "Django Unchained": {
#         "John": 'ten',
#         "Jack": 'nine'
#     },
#
#     "Акыркы Сабак": {}
# }

# for k, v in movies.items():
#     for i in v:
#         movies[k][i] = movies[k][i].upper()
#     print(v)

# movies['Django Unchained']['John'] = movies['Django Unchained']['John'].upper()
# print(movies)

# a = lambda x: x + 2
#
# def b(x):
#     return x + 2

# print(a(5))
# print(b(5))


# words = ['Python', 'Exceptions', 'lambda']
# words.sort()
# print(words)

# words1 = ['conditions', 'operators', 'bool']
#
#
# def title_word(word):
#     print(word.title())
#     # return word.upper()
#
# def up_letters(word):
#     # print(word.upper())
#     return word.upper()
#
# def up_word(lst, func):
#     for i in lst:
#         print(func(i))
#
#
# up_word(words, up_letters)
# up_word(words, lambda x: x.upper())

# up_word(words1, title_word)