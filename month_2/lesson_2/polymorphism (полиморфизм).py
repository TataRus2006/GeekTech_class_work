# polymorphism (полиморфизм)


# def foo(x, y):
#     return x + y
#
#
# print(foo(32, 41))          # 73
# print(foo('32', '41'))      # 3241
# print(foo([32], [41]))      # [32, 41]


#
# class Animal:
#     legs = 4
#     tail = 1
#
#     def voice(self):
#         print('Какой-то звук')
#
#
# class Cat(Animal):
#     def cat_voice(self):
#         print('Мяу-мяу')
#
#
# class Dog(Animal):
#     def dog_voice(self):
#         print('Гав-гав')
#
#
# class Bull(Animal):
#     def bull_voice(self):
#         print('Мууу!')
#
#
# cat1, cat2 = Cat(), Cat()
# dog1, dog2 = Dog(), Dog()
# bull1, bull2 = Bull(), Bull()
#
# farm_band = [cat1, cat2, dog1, dog2, bull1, bull2]
#
# for i in farm_band:
#     if isinstance(i, Cat):
#         i.cat_voice()
#     if isinstance(i, Dog):
#         i.dog_voice()
#     if isinstance(i, Bull):
#         i.bull_voice()


class Animal:
    legs = 4
    tail = 1

    def voice(self):
        print('Какой-то звук')


class Cat(Animal):
    def voice(self):
        print('Мяу-мяу')


class Dog(Animal):
    def voice(self):
        print('Гав-гав')


class Bull(Animal):
    def voice(self):
        print('Мууу!')


cat1, cat2 = Cat(), Cat()
dog1, dog2 = Dog(), Dog()
bull1, bull2 = Bull(), Bull()
an = Animal()


farm_band = [cat1, cat2, dog1, dog2, bull1, bull2, an]

for i in farm_band:
    i.voice()
