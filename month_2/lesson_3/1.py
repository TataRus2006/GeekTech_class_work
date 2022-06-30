class Num:
    def __init__(self, num):     # функция, метод
        self.num = num

    def __add__(self, other):
        print("method __add__ called")
        self.num += other
        return Num(self.num)
    #
    #
    # def __sub__(self, other):
    #     print("method __sub__ called")
    #     self.num -= other
    #     return Num(self.num)
    #
    #
    def __str__(self):
        return f'its instanse of Num: {self.num}'
    #
    #
    # def __repr__(self):
    #     return f'Num({self.num})'

num1 = Num(20)     # это объект

num2 = num1 + 20

print(repr(num2))
print(num2)



# class Lion:
#     def __init__(self, name):
#         self.name = name
#
# s = Lion("Bob")
#
# print(s)

