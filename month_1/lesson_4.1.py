students = [2, 3, 5, 6, 7, 9, 10, 12, 14]
data = list()


while len(students) != 0:
    print(students)
    id = int(input('ввведите id студента: '))
    if id == 0:
        print('exit...')
        break
    students.remove(id)
    name = input('имя студента: ').title()
    rate = int(input(f'оценка для {name}: '))
    data.append([name, rate])

c = 0
for i in data:
    c += i[1]
    print(i)

print('средняя оценка: ', c / len(data))

# other = ['tuple', 'loop', 'abc', 'we']
#
# new = sorted(other)
# print(new)
#
# objects1 = list()
# objects = [2, 7.9, 3, 34, 56]

# print(objects.index('Samat'))
# print(objects)

# objects.reverse()
# objects.sort(reverse=True)
#
# print(objects.count(3))
#
# print(objects)


'''Удаление'''
# deleted = objects.pop(objects.index('Samat'))
# objects.remove(True)
# del objects[0], objects[3-1]


"""добавление"""
# other[0] = other[0][:4]
# objects.extend(other)
# objects.append('geektech')
# objects.insert(1, 'list')
# objects[-2].append(345)


"""изменение"""
# objects[0] = 10
# objects[1], objects[2] = 8.0, False
# objects[2], objects[3] = objects[3], objects[2]


"""Индексация, срезы"""
# new = objects[::1]
#
# print(id(objects))
# print(id(new))
#
# print(new == objects)
# print(new is objects)
#
#
# print(objects[2:])
# print(objects[-1])

# print(type(objects))

# ['Urmat', 1]
# ['Sultan', 4]
# ['Ильяс', 3]
# ['Эрзат', 4]
# ['Абдулла', 3]
# ['Самара', 3]
# ['Улук', 4]
# ['Айкол', 4]
# ['Usen', 2]