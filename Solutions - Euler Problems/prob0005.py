"""
Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Answer: 232792560
"""


def smallest_number_divisible_by_range(a, b):
	answer = 2
	divisors = range(a, b + 1)
	for x in divisors:
		if answer % x != 0:
			for y in divisors:
				if (answer * y) % x == 0:
					answer *= y
					break
	return answer

print smallest_number_divisible_by_range(1,20)