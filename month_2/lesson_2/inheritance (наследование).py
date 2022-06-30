# inheritance (наследование)


class Vehicle:
    def __init__(self, name, model, **kwargs):
        self.name = name
        self.model = model
        if 'passenger' in kwargs:                                # passenger - пассажир (пассажировместимость)
            self.passenger = kwargs['passenger']
        else:
            self.passenger = 1


class Car(Vehicle):
    def __init__(self, name, model, **kwargs):
        # self.name = name                                          # вместо name и model пишем инициализацию
        # self.model = model                                        # родительского класса с помощью метода super()
        super().__init__(name, model, **kwargs)
        if 'fwd' in kwargs:                                         # fwd - наличие полного привода
            self.fwd = kwargs['fwd']
        else:
            self.fwd = False


class Plane(Vehicle):
    def __init__(self, name, model, **kwargs):
        super().__init__(name, model, **kwargs)
        if 'max_height' in kwargs:                                        # max_height - максимальная высота
            self.max_height = kwargs['max_height']
        else:
            self.max_height = 10000


audi = Car('Audi', 'A4 3.0', passenger= 5)
print(audi.__dict__)
airbus = Plane('Airbus', 'A320', passenger=176)
print(airbus.__dict__)