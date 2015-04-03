"""
10001st prime
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

Answer: 104743
"""

import math

def is_prime(number):
    x = 2
    while x < int(math.sqrt(number))+1:
        if number % x == 0:
            return False
        else:
            x+=1
    return True

def get_nth_prime(n):
    x = 0
    i = 2
    while True:
        if is_prime(i) is True:
            x += 1
            if x == n:
                return i
        i += 1

print get_nth_prime(2)