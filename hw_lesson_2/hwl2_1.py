# запит у юзера на введення 4-х значного числа
number = int(input("Enter number from 0000 to 9999: "))
# вираховуємо послідовно кожну цифру числа number
digit1 = number // 1000
digit2 = number % 1000 // 100
digit3 = number % 100 // 10
digit4 = number % 10
# виводимо послідовно кожну цифру числа number
print(digit1)
print(digit2)
print(digit3)
print(digit4)