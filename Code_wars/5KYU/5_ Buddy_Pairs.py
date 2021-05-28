import math
from collections import defaultdict
beginning = defaultdict()

def buddy1(start, limit):
    for i in range(start, limit + 1):
        summa = 0
        for j in range(1, i):
            if i % j == 0:
                summa += j
            if summa > i:
                beginning[i] = summa

        for k in beginning.keys():
            if beginning[i] - 1 == k and beginning[k] - 1 == i:
                return [k, i]

        # if no match found continue search.

    for i in range(limit, 100000):
        summa = 0
        for j in range(1, i):
            if i % j == 0:
                summa += j
        for k in beginning.keys():
            if summa - 1 == k and i == beginning[k] - 1:
                print(beginning)
                return [k, i]


def divisor(x):
    return sum(set(d for pair in ([i, x//i] for i in range(1, int(x**0.5)+1) if not x % i) for d in pair)) - x


def buddy(start, limit):
    for i in range(start, limit + 1):
        summa = divisor(i)

        if summa > i + 1:

            lookup = summa - 1
            look_sum = divisor(lookup)

            if look_sum - 1 == i:
                return [i, lookup]

    return "Nothing"


print(buddy(48, 50))
print(buddy(2177, 4357))
print(buddy(57345, 90061))
print(buddy(1071625, 1103735))
