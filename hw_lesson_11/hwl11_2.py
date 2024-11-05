def generate_cube_numbers(end):
    count = 2#починаємо з 2
    number = count#фіксуємо число для зведення в степінь
    while True:
        count = number**3
        if count > end:#вихід згідно умови
            return
        yield count
        number += 1

from inspect import isgenerator

gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'
print('OK')