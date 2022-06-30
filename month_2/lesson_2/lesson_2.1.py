class Animals:
    def __init__(self, name, voice_text):
        self.name = name
        self.voice_text = voice_text
    def voice(self):
        print(f"{self.name} {self.voice_text}")


class Dog(Animals):
    pass

class Cat(Animals):
    pass

sharik = Dog("Sharik", "GAF GAF!")
murka = Cat("Murka", "MEW MEW!")

sharik.voice()
murka.voice()