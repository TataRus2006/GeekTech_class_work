# Функции, аргументы: *args, **kwargs.



# def menu(**kwargs):
#     return kwargs
#
# print(menu(one=1, two=2))
#
#
# def sum1(b, *args, c=2):
#     # print(type(args))
#     print('b - ', b)
#     print('c - ', c)
#     print('args - ', args)
#     return sum(args) - b * c
#
# print(sum1(2, 3, 1, 5, 4))




# def menu():
#     meals = ['плов', "манты", "лагман"]
#     drinks = ['cola', 'tea', 'water', 'juice']
#     while True:
#         choice_eat = int(input(f'Выберите еду по индексу: \n {list(enumerate(meals))}'))
#         choice_drink = int(input(f'Выберите напиток по индексу: \n {list(enumerate(drinks))}'))
#         return {'drink': drinks[choice_drink], 'eat': meals[choice_eat]}
#
#
# monday = menu()
# tuesday = menu()
# friday = menu()
#
# print(monday, tuesday, friday)



# def greet(name, age=18):
#     print(f'Hello {name}!\n'
#           f'{2022 - age}')
#     # return 'Hello World!'
#
# greet('Samat', 45)


# def get_square(l, w):
#     return l * w
# kitchen = get_square(4, 3)
# hall = get_square(6, 5)

# print(kitchen)

# def find_five(lst):
#     c = 1
#     for i in lst:
#         if i == 5:
#             print(c)
#             return f'индекс первой пятерки: {lst.index(i)}'
#         c += 1
#     else:
#         return False
# print(find_five(a))

# print(find_five(b))

# def f(a, b, c):
#     return a * b - c
#
#
# print(f(1, 2, 3))
# print(f(a=1, c=3, b=2))
