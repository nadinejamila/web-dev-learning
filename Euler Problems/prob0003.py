"""
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

Answer: 6857

"""

original = 600851475143

def get_minimum_factor(number):
    x = 2
    while x < number:
        if number % x == 0:
            return x
        else:
            x+=1
    return False

def get_largest_prime_factor(number):
    factor = 1
    while factor:
        number = number/factor
        factor = get_minimum_factor(number)
    return number

print get_largest_prime_factor(original)