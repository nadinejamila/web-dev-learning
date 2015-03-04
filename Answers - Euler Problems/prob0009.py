"""
PROBLEM 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def product_of_triplet(target):
	for a in range(1, target + 1):
		for b in range(1, target + 1):
			if a + b < target:
				c = (a**2 + b**2)**0.5
				if c % 1 == 0: #if it is a perfect square
					sum_ = a + b + c
					if sum_==target:
						product = a * b * c
						return product
	return 'No answer found'
		
print 'The answer is',				
print product_of_triplet(1000)