def is_even(number):
    last = str(number)[-1]#берем крайню цифру числа і перевіряємо далі на рівність до 0,2,4,6,8
    if last == "0" or last == "2" or last == "4" or last == "6" or last == "8":
        return True
    else:
        return False

assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print('OK')