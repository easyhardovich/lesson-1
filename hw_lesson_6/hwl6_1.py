# Користувач вводить через дефіс дві літери, Ваше завдання написати програму, яка повертатиме всі символи між ними включно.
# Жодних перевірок на помилку робити не треба, мінімальне значення завжди менше або дорівнює максимальному.
# Підказка: Використовуйте модуль string , у якому є string.ascii_letters, з усім набором потрібних букв

import string

for_letters = string.ascii_letters
user_choise = input()

print(for_letters[for_letters.find(user_choise[0]):for_letters.find(user_choise[2])+1])