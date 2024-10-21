# Ваше завдання – написати функцію is_palindrome, яка перевірятиме, чи є рядок паліндромом.
# Паліндромом - це такий рядок, який читається однаково зліва направо і зправа наліво без урахування знаків пунктуації та розмірності букв.
# Функція приймає на вхід рядок, та повертає булеве значення True або False
# Приклад:
import string
for_punctuation = string.punctuation

def is_palindrome(text):
    text_for_check = ""
    for char in text:#наповнюємо строку для перевірки
        if for_punctuation.find(char) < 0:
            text_for_check = text_for_check + char
    text_for_check.replace(" ", "")
    #якщо строка співпадає зі своїм оберненим варіантом, то True, інше False
    if text_for_check.lower().replace(" ","") == text_for_check.lower().replace(" ","")[::-1]:
        return True
    else:
        return False

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")