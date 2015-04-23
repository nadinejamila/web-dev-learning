
# The raw_input prompts the user to enter data into the terminal.
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

# The data entered before can be printed out later on like this.
print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)