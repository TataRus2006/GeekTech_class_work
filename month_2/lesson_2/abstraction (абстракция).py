# abstraction (абстракция)


# # 1000 : 15 = mass : x
# # x = mass * 15 :1000
#
#
# def get_salt_mass(m):
#     return m * 15 / 1000
#
#
# def get_pepper_mass(m):
#     return m * 5 / 1000
#
#
# print(get_salt_mass(1500))
# print(get_pepper_mass(1200))
#


# ingridients = {
#     'salt': 15,
#     'pepper': 5
# }
#
#
# def get_ingridients_mass(m, ingr):
#     # return m * ingridients[ingr] / 1000
#     return m * ingridients.get(ingr, 0) / 1000
#
#
# print(get_ingridients_mass(1500, 'salt'))
# print(get_ingridients_mass(1200, 'pepper'))
# print(get_ingridients_mass(1100, 'chili'))
#


# def print_wrapper(text):
#     with open('readme', 'a') as file:
#         print(text, file=file)
#         # \n - переход на новую линию        \n = new line
#
# print_wrapper(2)
#



#print включает в себя: value, ..., sep=' ', end='\n', file=sys.stdout, flush=False
# value - значение,
# sep=' ' - sep: строка, вставляемая между значениями, по умолчанию пробел,
# end='\n' - end: строка, добавляемая после последнего значения, по умолчанию - новая строка.
# file=sys.stdout - file: файлоподобный объект (поток); по умолчанию используется текущий sys.stdout.
# flush=False -  flush: нужно ли принудительно очищать поток