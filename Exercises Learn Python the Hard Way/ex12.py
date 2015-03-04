# we can either print out the question first, or put it inside the raw_input function.
age = raw_input("How old are you? ")
height = raw_input("How tall are you?")
weight = raw_input("How much do you weight?")

print "So you're %r old, %r tall and %r heavy." % (
	age, height, weight)