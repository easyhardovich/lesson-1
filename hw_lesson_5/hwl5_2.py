# Модифікувати калькулятор таким чином, щоб він працював доти, доки користувач цього хоче.
# Тобто, потрібно робити запит до користувача на продовження роботи калькулятора після кожного обчислення -
# якщо користувач ввів yes (можна просто y), то нове обчислення, інакше - закінчення роботи.

#вводимо два числа та обираємо дію
#цикл для можливості реалізації повторюваних дій
while 0 == 0:
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    action = int(input("1. +\n2. -\n3. *\n4. /\nСhoose a math operation: "))

    match action:
        case 1:
            print(first_number + second_number)
        case 2:
            print(first_number - second_number)
        case 3:
            print(first_number * second_number)
        case 4:
            if second_number == 0:
                print("Cannot be divided by 0")
            else:
                print(first_number / second_number)

    # запитуємо необхідність виконання інших операцій
    question = str(input("Type 'yes' or 'y' to do enother operation: "))
    # перевірка введеного вибору для наступних операцій
    if question == "yes" or question == "y":
        continue
    else:
        break