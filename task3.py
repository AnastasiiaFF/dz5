"""
Создайте функцию генератор чисел Фибоначчи
"""

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

n = int(input('введите кол-во чисел  Фибоначчи: '))

f = fibonacci()
for _ in range(n):
    print(next(f), end=' ')