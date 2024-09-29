# запит у юзера на введення 5-ти значного числа
number = int(input("Enter number from 00000 to 99999: "))
# вираховуємо послідовно кожну цифру числа number
digit1 = number // 10000
digit2 = number % 10000 // 1000
digit3 = number % 1000 // 100
digit4 = number % 100 // 10
digit5 = number % 10
# виводимо number із зворотною послідовністю цифр
print(f"{digit5}{digit4}{digit3}{digit2}{digit1}")

