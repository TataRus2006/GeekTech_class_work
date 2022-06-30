# # class User:
# #
# #     def __init__(self, first_name, last_name, age):
# #         self.first_name = first_name
# #         self.last_name = last_name
# #         self.age = age
# #
# # jack = User("Jack", "Barboro", 20) # Instance User
# # print(jack.first_name, jack.last_name, jack.age)
#


# class Car:
#     def __init__ (self, title, model, color):
#         self.title = title
#         self.model = model
#         self.color = color
# mers = Car("mers", "s500", "black")
# print(mers.title, mers.model, mers.color)
class Car:
    def __init__ (self, title, model, engine, max_speed, speed, ):
        self.title = title
        self.model = model
        self.engine = engine
        self.max_speed = max_speed
        self.speed = speed
        self.current_speed = 0

    def gas(self):
       if self.current_speed + self.speed >= self.max_speed:
           print('Check ON')
       else:
           self.current_speed += self.speed
           print(f"Current speed = {self.current_speed}")

    def get_info(self):
        print(f"""
Title: {self.title} {self.model}
Engine: {self.engine}
Max Speed: {self.max_speed}
        """)




bmw = Car("BMW", "e38", "v10", 360, 20)
bmw.get_info()
bmw.gas()
bmw.gas()
bmw.gas()
bmw.gas()
bmw.gas()



# print(bmw)

# mers = Car("mers", "s500", "5.0", 320, 15)
# mers.get_info()
# # print(mers.title, mers.model, mers.engine, mers.max_speed, mers.speed)
# Создать классы машин допустим (Bmw, Mercedes)
# определить такие атрибуты как (title, model, weight, hp, nm, max_speed, color)
# создать метод start_engine() -> output title + model engine started!
# создать метод stop_engine() -> output title + model engine stopped!
# создать метод info() -> All Info

# class Car:
#     def __init__(self, title, model, weight, hp, nm, max_speed, color):
#         self.title = title
#         self.model = model
#         self.weight = weight
#         self.hp = hp
#         self.nm = nm
#         self.max_speed = max_speed
#         self.color = color
#
#     def start_engine(self):
#         print(f"""
# Output:{self.title} {self.model} engine started!
#                 """)
#
#     def stop_engine(self):
#         print(f"""
# Output: {self.title} {self.model} engine stopped!
#                 """)
#
#     def all_info(self):
#         print(f"""
# Title: {self.title} {self.model}
# Weihht: {self.weight}
# Hp / Nm: {self.hp} / {self.nm}
# Speed: {self.max_speed}
# Color: {self.color}
#                 """)
#
# bmv = Car("BMW", "M5", "2750 кг", 560, 5750, 250, "blue")
# bmv.start_engine()
# bmv.stop_engine()
# bmv.all_info()
#
# merc = Car("Mercedes", "X350", "3250 кг", 258, 3400, 205, "Grey")
# merc.start_engine()
# merc.stop_engine()
# merc.all_info()

