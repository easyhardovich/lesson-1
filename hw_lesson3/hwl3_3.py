#початковий список
numbers = [1, 2, 3, 4, 5]
#розділений список
numbers2 = []

if len(numbers) == 0:#список порожній
    numbers2.append(numbers[:])
    numbers2.append(numbers[:])
elif len(numbers)%2 == 0:# у списку парна кількість елементів
    numbers2.append(numbers[:len(numbers) // 2])
    numbers2.append(numbers[len(numbers) // 2:])
else:#в списку непарна кількість елементів
    numbers2.append(numbers[:len(numbers)//2 + 1])
    numbers2.append(numbers[len(numbers)//2 + 1:])
#виводимо розділений список
print(numbers2)