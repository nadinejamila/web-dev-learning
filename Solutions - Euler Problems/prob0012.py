"""Highly divisible triangular number
Problem 12
The sequence of triangle numbers is generated by adding the natural numbers. 
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. 
The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?

Answer: 76576500 
"""
import time
import math


def get_factors(n):
    # This gets the factors of the number, testing from 1 until its square root.
    factors = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors += 2
    return factors


def get_triangular_number(n):
    # A triangular number is a number obtained by adding all positive integers
    # less than or equal to a given positive integer n
    return n*(n+1) / 2


def get_triangular_num_with_over_n_divisors(n):
    counter = 1
    while True:
        number = get_triangular_number(counter)
        factors = get_factors(number)
        if factors > n:
            return number
        counter +=1


start = time.time()
answer = get_triangular_num_with_over_n_divisors(500)
elapsed = (time.time() - start)
print "Answer: %s \nElapsed time: %s" % (answer, elapsed)