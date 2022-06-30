data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')

letters = []
numbers = []

for i in data_tuple:
    if type(i) == str:
        letters.append(i)
    else:
        numbers.append(i)

numbers.remove(6.13)
# del numbers[0]

return_True = numbers.pop(0)
letters.append(return_True)
numbers.insert(1, 2)
numbers.sort()
letters.reverse()
letters[letters.index('g')] = 'G'
letters[letters.index('C')] = 'c'
new_numbers = []

for i in numbers:
    i = i**2
    new_numbers.append(i)
numbers = new_numbers

letters = tuple(letters)
numbers = tuple(numbers)
print(letters)
print(numbers)

