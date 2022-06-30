class Transport:
    def __init__(self, title, engine, color, model, tachometr):
        self.title = title
        self.engine = engine
        self.color = color
        self.model = model
        self.tachometr = tachometr


    def start_engine(self):
        print(f"On {self.title} {self.model} engine started!")


    def stop_engine(self):
        print(f"On {self.title} {self.model} engine stopped!")


    def car_check(self):
        if self.tachometr < 1:
            print("Check On!")
        else:
            print("Check OFF!")
class Car(Transport):
    def __init__(self, title, engine, color, model, tachometr, max_speed):
        super().__init__(title, engine, color, model, tachometr)
        self.max_speed = max_speed


class Tesla(Car):
    pass



tesla = Tesla("Tesla", "electra car","black", "plaid", 1, 250)
# tesla.stop_engine()
# tesla.car_check()

print(tesla.max_speed)