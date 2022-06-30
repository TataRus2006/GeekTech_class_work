# dict = {key: value}
# letters = ['a', 'b', 'e', 'c', 'd', 'e', 'a']



# print(ing)
# a = 'мясо лук'.split()
# a = set(a)

# menu = {
#     'steak': {"мясо", "картофель", "соус"},
#     "манты": {'мясо', "лук", "тесто"},
#     'свежий': {'томат', "огурец", "лук"}
# }
#
# ing = input('Введите ингридиент: ').split()
# ing = set(ing)
#
#
# for k, v in menu.items():
#     if ing.intersection(v):
#         print(k)

# kyrgyzstanec = {'kyr', 'rus', 'eng'}
# kazakh = {'rus', 'eng', 'kaz'}
#
# print(kyrgyzstanec.difference(kazakh))
# print(kyrgyzstanec - kazakh)
#
# print(kyrgyzstanec.intersection(kazakh))
# print(kyrgyzstanec & kazakh)
# #
# # print(kyrgyzstanec.union(kazakh))
# # print(kyrgyzstanec | kazakh)
# #
# print(kyrgyzstanec.symmetric_difference(kazakh))
# print(kyrgyzstanec ^ kazakh)


# names = ('Сатылганов', "Датка", "Т.Молдо", "Тыныстанов")
# numbers = (100, 50, 20, 10)
#
# data = {}
# c = 0
# while c != len(names):
#     data[numbers[c]] = names[c]
#     c += 1
#     for k, v in data.items():
#         print(f'{k} - {v}')


# student = {
#     'name': 'Azamat',
#     'age': 23,
#     'hobby': ['chess', 'boxing'],
#     'job': 'мясник'
# }
#
# student2 = dict(name='Alina', age=22, hobby=['cook', 'ride'])
#
#
# for k, v in student.items():
#     print(f'{k}: {v}')

# print(student.keys())
# print(student.values())
# print(student.items())


# student['surname'] = 'Жыргалбеков'
# student.update(student2)
#
# student['age'] = 24
#
# del student['surname']
# new = student.pop('job')


# print(student.get('hobb', "нет такого!"))
# print(type(student))

    # 1: 'one',
    # True: [1, 2, 3],
    # (1, 2): ('a', 'b', 'c')
