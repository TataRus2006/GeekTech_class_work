ten = list(range(1, 11))
evens = list(filter(lambda x: x % 2 == 0, ten))
evens_squared = list(map(lambda x: x * x, evens))
print(evens_squared)
lst_numbers = (ten, evens, evens_squared)

def show(list):
    while True:
        try:
            command = int(input('enter index: 0 - "ten", 1 - "evens", 2 "evens_squared" 77 выход из программы \n'))
            print(list)
            show(list[command])
        except ValueError:
                print('НЕ ВВОДИТЬ БУКВЫ!')
        except IndexError:
                print(f"вводить только числа! от 0 - {len(list) - 1}")



#         if command == 77:
#             print('Произведен выход!')
#             break
#             else:
#                 print('Вы неверно указали индекс! Введите индекс в цифровом формате от 0 до 2 или q для выхода из программы')
#         elif command.isdigit():
#             show(lst_numbers[int(command)])
#
# def show(list=ten):
#     while True:
#         try:
#             command = int(input('enter index: \n'))
#             if command == 77:
#                 print('stop program')
#                 break
#             print(list[command])
#         except ValueError:
#             print('НЕ ВВОДИТЬ БУКВЫ!')
#         except IndexError:
#             print(f"вводить только числа! от 0 - {len(list) - 1}")
#
#
show(lst_numbers)