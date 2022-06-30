# dict = {key: value}

menu = {
    "манты": {'мясо', "тесто", "лук"},
    "плов": {"рис", "мясо", "морковь"},
    "бешбармак": {"лапша", "мясо", "лук"},
    "свежий": {"помидор", "огурец", "зелень"}
}

while True:
    ing = input('Введите ингридиент: ')
    for k, v in menu.items():
        if ing in v:
            print(k)




# kg = {'yellow', 'red'}
# rus = {'white', 'blue', 'red'}
#
# print(kg.intersection(rus))
# print(kg & rus)
#
# print(kg.union(rus))
# print(kg | rus)
#
# print(kg.difference(rus))
# print(kg - rus)
#
# print(kg.symmetric_difference(rus))
# print(kg ^ rus)


# print(set('stoppa'))
# numbers = [1, 2, 3, 4, 2, 2, 1, 'stopp']
# numbers2 = {2, 1, 3, 4, 2, 2, 1, 'stopp'}
#
# print(numbers)
# print(numbers2)
# print(type(numbers2))


# worker = dict(name='Jack', age=45, job='engineer')
# # print(worker)
#
# student = {
#     'name': 'Alex',
#     'age': 34,
#     'job': ['student', 'waiter'],
#     'active': True,
#     'first_year': {"математика": 4, "физике": 5},
# }
#
# print(student)

# search = input('введите данные: ')
# for i in student.items():
#     if search in i:
#         print("нашли - ", i)
#         new_job = 'teacher'
#         ind = student['job'].index('student')
#         student['job'][ind] = new_job
#         break
#
# print(student)



    # if search == v:

# print(student.keys())
# print(student.values())
# print(student.items())


# print(student['nam'])
# print(student.get('nam', 'такого ключа нет'))


# student['last_name'] = 'Jackson'
# worker.update(student)

# del student['active']

# new = student.pop('first_year')
# print(new)