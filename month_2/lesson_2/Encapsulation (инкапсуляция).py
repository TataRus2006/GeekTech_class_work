# Encapsulation (инкапсуляция) - сокрытие реализации от пользователя (для безопасности и целостности объекта)

                                # public (публичный) уровень доступа

# class Kettle:                                 # Kettle - чайник
#     def turn_on(self):
#         print('Нажали кнопку')
#         self.boil()
#         self.check_temperature()
#         self.beep()
#         self.turn_off()
#
#
#     def boil(self):
#         print('Разогревание воды')
#
#
#     def check_temperature(self):
#         print('Проверяем температуру воды')
#
#
#     def beep(self):
#         print('Проверяем звуковой сигнал')
#
#
#     def turn_off(self):
#         print('Автоматическое отключение')
#
#
# my_kettle = Kettle()
#
# my_kettle.turn_on()
# my_kettle.boil()
# my_kettle.check_temperature()
# my_kettle.beep()
# my_kettle.turn_off()




                                # protected уровень доступа
# class Kettle:                               # Kettle - чайник
#     def turn_on(self):
#         print('Нажали кнопку')
#         self.__boil()
#         self.__check_temperature()
#         self.__beep()
#         self._turn_off()
#
#
#     def __boil(self):
#         print('Разогревание воды')
#
#
#     def __check_temperature(self):
#         print('Проверяем температуру воды')
#
#
#     def __beep(self):
#         print('Проверяем звуковой сигнал')
#
#
#     def _turn_off(self):
#         print('Автоматическое отключение')
#
#
# my_kettle = Kettle()
# # my_kettle.turn_on()
# my_kettle._turn_off()       # нештатное использование объекта
#

                                # private (частный) уровень доступа
#
# class Kettle:                               # Kettle - чайник
#     def turn_on(self):
#         print('Нажали кнопку')
#         self.__boil()
#         self.__check_temperature()
#         self.__beep()
#         self.__turn_off()
#
#
#     def __boil(self):
#         print('Разогревание воды')
#
#
#     def __check_temperature(self):
#         print('Проверяем температуру воды')
#
#
#     def __beep(self):
#         print('Проверяем звуковой сигнал')
#
#
#     def __turn_off(self):
#         print('Автоматическое отключение')
#
#
# my_kettle = Kettle()
# my_kettle.turn_on()             # доступен только один метод, все остальные методы будут вызываться самим
#                                 # объектом если это необходимо и предпологается логикой класса
#


my_kettle._Kettle__beep()  

