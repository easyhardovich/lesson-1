
def is_prime(x):#допоміжна функція для визначення простоти числа
    for i in range(2, (x // 2) + 1):#перевіряємо дільники до половини числа
        if x % i == 0:#якщо число ділиться без залишку на дільники крім себе то воно не просте
            return False
    return True#якщо число не поділилось без залишку то воно просте

def prime_generator(end):
    begin = 2
    number = begin
    while begin <= end:
        if is_prime(begin) == True:#якщо число проходить перевірку враховуємо його генератором
            yield begin
        begin += 1

from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')