# Створіть список випадкових чисел із випадковою кількістю елементів від 3 до 10.
# Ваше завдання - створити новий список з 3 елементів початкового списку - першим, третім і другим з кінця.
import random

firstlist = []
# наповнюємо перший список
i = 0
while i < random.randint(3, 10):
    firstlist.append(random.randint(0, 9))
    i += 1
# створюємо новий список
secondlist = []
# наповнюємо другий список трьома елементами початкового списку - першим, третім і другим з кінця
secondlist.append(firstlist[0])
secondlist.append(firstlist[2])
secondlist.append(firstlist[-2])
print(firstlist, end = " == ")
print(secondlist)