class Car:
    def __init__(self, title, model, max_speed, speed):
        self.title = title
        self.model = model
        self.max_speed = max_speed
        self.speed = speed
        self._current_speed = 0

    def start_engine(self):
        print(f'{self.title} {self.model} engine started!')

    def gas(self):
        if self._current_speed + self.speed < self.max_speed:
            self._current_speed += self.speed
            

BMW = Car("BMW", "b7", 350, 20)
print(BMW._current_speed)
