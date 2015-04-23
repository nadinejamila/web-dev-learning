"""
Multiples of 3 and 5
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Answer: 233168
"""

def sum_of_multiples_of_x_y(x, y, limit):
	total = 0
	for number in range(1, limit):
		if number % x == 0 or number % y == 0:
			total += number
	return total

print sum_of_multiples_of_x_y(3, 5, 1000)


