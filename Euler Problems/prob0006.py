"""
Sum square difference
Problem 6

The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

Answer: 25164150
"""

def sum_of_squares(a, b):
	total = 0
	for x in range(a, b + 1):
		total +=  x * x
	return total

def square_of_sum(a, b):
	total = sum(range(a, b + 1))
	return total * total

answer = square_of_sum(1, 100) - sum_of_squares(1, 100)

print answer