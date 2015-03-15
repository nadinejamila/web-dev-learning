"""
Summation of primes
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""

def prime_sieve(limit):
	""" 
	This function follows the Sieve of Erastosthenes to return 
	all the prime numbers below the limit value.
	"""

	# We make a list representing all numbers from zero to the limit - 1
	numbers = [True] * limit
	
	# 0 and 1 are not primes
	numbers[0] = False
	numbers[1] = False

	# We use enumerate to get the index of the list item 
	# which also represents its numberical value
	for i, is_prime in enumerate(numbers):
		# If the item represents a prime number (i.e. True),
		# its multiples starting from its square up to the limit is 
		# deemed as a non-prime number (therefore, False). 
		if is_prime:
			for n in xrange(i*i, limit, i):
				numbers[n] = False

	return numbers

def get_sum(numbers):
	"""
	This function gets the sum of all the prime numbers by 
	summing the indices of a list wherein 'True' represents a prime number
	as its index.
	"""
	total = 0
	for i, is_prime in enumerate(numbers):
		# if the value is True, the index of that element is 
		# prime and is therefore added to the total value
		if is_prime:
			total += i
	return total

limit = 2000000
primes = prime_sieve(limit)
print get_sum(primes)