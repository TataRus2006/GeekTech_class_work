""""
Modules - ?
"""

# import my_module # импортирует весь документ
#
# from  my_module import secret_key # импортирует определенный объект
#
# print(secret_key)
#
# print(my_module.secret_key)
#
# from  my_module import message, Dog
#
# message('Hello word')
#
# Sharik = Dog('Sharik', 0.5, 20, 'gaf gaf')
#
# print(Sharik)


# from person import models, create_person
# from person.models imporn Person
# models.Person


from person.create_person import create_person

jack = create_person(
        first_name='Jack',
        last_name='Barboro',
        age=20
)

jack.info()
