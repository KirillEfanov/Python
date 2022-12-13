from math import prod
from random import randint
from statistics import median

print("1 задание")
sum_row = 0
for i in range(0, 999999 + 1):
    sum_row += i
print("Сумма ряда 0 - 999999 равна: ", sum_row, '\n')
print("2 задание")
medium = sum_row / 1000000
print("Среднее ряда: ", medium, '\n')
print("3 задание")
random = []
for i in range(1000000):
    random.append(randint(1, 10))
print("Медиана ряда 1000000 случайных чисел от 1 до 10: ", median(random), '\n')
print("4 задание")
print("Их произведение: ", prod(random))
