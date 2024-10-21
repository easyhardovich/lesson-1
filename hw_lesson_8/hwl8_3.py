# Вам необхідно написати функцію find_unique_value, яка приймає список із чисел,
# знаходить серед них унікальне число та повертати його. Унікальне число - це число,
# яке зустрічається в списку один раз.
# Випадок, коли в одному списку буде кілька унікальних чисел, перевіряти не потрібно.
import math
from itertools import count

def find_unique_value(some_list):
    min_count = math.inf
    unique_number = some_list[0]#якщо елемент у списку один то він і є унікальним по суті
    for element in some_list:
        if some_list.count(element) == 1:#якщо знайдемо елемент який зустрічається один раз то перезапишемо його як найменший
            unique_number = element
    return unique_number

assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")