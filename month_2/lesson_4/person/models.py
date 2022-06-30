class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def info(self):
        print(f"""
        First_name: {self.first_name}
        Last_name: {self.last_name}
        Age: {self.age}
        """)

