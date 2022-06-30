# dict = {key: value}

# new_dict = dict()

#1
worker = dict(name='jack', age=45, job='engineer')
print(worker)

#2
student = {
    'name': 'Alex',
    'age': 20,
    'job': ['student', 'waiter'],
     # 2: 'two'
    'active': True,
    'first_year': {"математика": 4, "физика": 5}
}

student['lastname'] = 'Jackson'
student.update(worker)

print(student)
