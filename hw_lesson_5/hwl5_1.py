# Користувач вводить рядок. Ваше завдання - перевірити, чи може цей рядок бути ім'ям змінної.
#
# Змінна не може:
#
# починатися з цифри
# містити великі літери,
# пробіл і знаки пунктуації (взяти можна тут string.punctuation), окрім нижнього підкреслення "_".
# бути жодним із зареєстрованих слів.
# При цьому повне ім'я змінної повино складатись не більш чим з одного нижнього підкреслення "_".
#
# Список зареєстрованих слів можна взяти із keyword.kwlist.
#
# У результаті перевірки на друк виводиться або True, якщо таке ім'я змінної допустимо, або False - якщо ні.
#
# Приклади імен змінних та результат перевірки (=> на друк виводити не потрібно :))
import string
import keyword

#список знаків пунктуації
for_punctuation = string.punctuation
#список зареєстрованих слів
for_keywordlist = keyword.kwlist
#запитуємо бажаний пароль у користувача
user_row = str(input())
#перевірка першого символу на число
begin_digit = user_row[0].isdigit()
#перевірка чи всі символи в нижньому регістрі та обробка випадку з одним "_"
if len(user_row) == 1 and user_row.find("_") == 0:
    lower_case = True
else:
    lower_case = user_row.islower()
#задаємо змінні для наступних перевірок
is_punctuation = False
lower_space = 0
has_space = False
is_keyword = False

#цикл перевірки на знаки пунктуації, пробіл та кількість "_"
for i in user_row:
    if for_punctuation.find(i) >= 0 and i != "_":
        is_punctuation = True
    elif for_punctuation.find(i) >= 0:
        lower_space += 1
    elif  i == " ":
        has_space = True

#цикл перевірки приналежності до зареєстрованих слів
for i in for_keywordlist:
    if i == user_row:
        is_keyword = True

#True якщо всі True
#Перший символ не цифра, тільки в нижньому регісті, не містить знаків пунктуації, "_" максимум 1, не містить пробілів, не зареєстроване слово
print(all([begin_digit == False, lower_case == True, is_punctuation == False, lower_space <= 1, has_space == False, is_keyword == False]))