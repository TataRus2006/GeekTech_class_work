students = [3, 4, 5, 6, 7, 8, 10, 11, 13, 14, 15, 16, 17]
data = []

while len(students) != 0:
    print(students)
    id = int(input("выберите номер: "))
    if id == 0:
        print('выход!')
        break
    students.remove(id)
    name = input('имя студента: ').title()
    rate = int(input('введите оценку'))
    data.append([name, rate])
    print("Data: " data)

for i in data:
    print(i)





# a = [1, 2, 3]
# b = (4, 5, 6)
# a.append(7)
# a = tuple(a)
#
# a += b
# print(a)
# print(b)

# students_2 = list()
# objects = ['abc', 2, 5, 2.4, True, []]
# new = objects
# cutted = objects[::1]


# objects.reverse()


# objects[-1].append(objects.pop(1))
# objects.append(objects.pop(1))


# i = 0
# while i < len(objects):
#     print(objects[i])
#     i += 1

# for i in objects:
#     print(i)


# objects[0] = objects[0].replace('b', 'B')
# objects[1], objects[3] = objects[3], objects[1]


"""Удаление"""
# objects.remove(2.4)
# deleted = objects.pop(objects.index(True))
# del objects[0], objects[1]
# print(deleted)



"""добавление"""
# objects.append('python')
# objects.insert(2, 'geektech')
# two = [4.5, False]
# objects.extend()
# objects += two


# print(id(objects))
# print(id(new))
# print(id(cutted))
#
# print(cutted == objects)
# print(cutted is objects)
# print(objects is new)

# print(objects[2:])
# print(objects[0][1])



# print(type(objects))


# ['Насирдин', 3]
# ['Марлен', 5]
# ['Эмир', 1]
# ['Шахмина', 4]
# ['Рустам', 5]
# ['Амина', 2]
# ['Вова', 4]
# ['Аделина', 2]
# ['Канатбек', 3]
# ['Сайрагуль', 4]
# ['Актан', 5]
# ['Нурия', 5]
# ['Арлен', 5]