import random

#задаємо список
numbers = []

#наповнюємо список рандомними значеннями, наприклад щоб довжина списку була до 5-ти значень
i = random.randint(0, 5)

while i > 0:
    numbers.append(random.randint(0, 9))
    i -= 1

#отримуємо заповнений вхідний стисок
print("Початковий список", end=' ')
print(numbers)
#переносимо останній елемент сиску на початок
if len(numbers) > 1:
    numbers.insert(0, numbers[-1])
    numbers.pop()
    print("Список після обробки", end=' ')
    print(numbers)
else:
    print("0 та 1 елемент без змін", end=' ')
    print(numbers)