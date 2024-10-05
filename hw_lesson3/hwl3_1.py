#вводимо два числа та обираємо дію
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