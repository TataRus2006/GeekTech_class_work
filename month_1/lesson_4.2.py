# списки, кортежи
# удаление по имени или индексу


names = ['Азамат', 'Самат', 'Алия']

del_name = input('Введите имя или индекс: ')

if del_name.isalpha():
    names.remove(del_name)
elif del_name.isdigit():
    del names[int(del_name)]
print(names)
