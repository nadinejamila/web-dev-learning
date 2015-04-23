print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from inutition
and requires an explanation
\n\t\twhere there is none.
"""

print '--------------'
print poem
print '--------------'

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
	# This returns the calculated variables when the function is called.
	jelly_beans = started * 500
	jars = jelly_beans
	crates = jars / 100
	return jelly_beans, jars, crates


start_point = 10000

# This assigns the return value of the formula into variables which we can use later on.
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"

# This prints out the return value of the function secret_formula()
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point) 