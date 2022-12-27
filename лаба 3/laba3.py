from pyDatalog import pyDatalog
from random import randrange
import math

pyDatalog.create_terms('sum_numbers, N, Sum_numbers, average_row, Average_row, row_random_numbers, median_random_numbers, Median_random_numbers, product, Product')

n = 1000000

print("1 задание: ")
sum_numbers[N] = N * N / 2
print(sum_numbers[n] == Sum_numbers)
print()

print("2 задание: ")
average_row[N] = sum_numbers[N] / N
print(average_row[n]==Average_row)
print()

row_random_numbers = []
for i in range(n):
    row_random_numbers.append(randrange(1, 10))
row_random_numbers.sort()

print("3 задание: ")
if n % 2 == 1:
    median_random_numbers = row_random_numbers[n//2]
else:
    median_random_numbers = (row_random_numbers[n//2 - 1] + row_random_numbers[n//2]) / 2
print(median_random_numbers==Median_random_numbers)
print()
