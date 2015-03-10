def while_loop(ceiling, increment):
	i = 0
	numbers = []

	while i < ceiling:
		print "At the top i is %d" % i
		numbers.append(i)

		i = i + increment
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	return numbers


def for_loop(ceiling, increment):
	numbers = []
	for i in range(0, ceiling, increment):
		numbers.append(i)
	return numbers


numbers = while_loop(12, 2)

print "The numbers using while-loop: "

for num in numbers:
	print num


numbers = for_loop(12, 2)

print "The numbers using for-loop: "

for num in numbers:
	print num

