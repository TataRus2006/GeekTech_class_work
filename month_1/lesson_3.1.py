# Циклы:
# for, while
# i (interable) -



        #for


# word = 'python'
# c = 1
#
# for letter in word:
#     print(letter, c)
#     c += 1
#

# numbers = '123456789'
# new = ''
#
# for i in numbers:
#     user = input('введите число')
#     if user == i:
#         new += i
#         print(new)
#     else:
#         continue



      #while

# c = 0
# while True:
#     print('hello', c)
#     c += 1

# circle = 0
# while True:
#     print(f'пробежали {circle} коугов!')
#     circle += 1
#     if circle == 5:
#         print('на сегодня хватит!')
#         break

# circle = 0
# while circle != 10:
#     print(f'пробежали {circle} кругов!')
#     circle += 1
#     if circle == 5:
#         print('перекур')
#         continue
#     elif circle == 8:
#         print('на сегодня все')
#         break
#

i = 0
new = ''
while True:
   start = input('Да или Нет?')
   numbers = '123456789'
   user = input('введите число:')
   if user.lower() == 'exit':
       print('finished')
       break
   if user == numbers[i]:
       new += numbers[i]
       print(new)
   else:
       print('повторите заново')


