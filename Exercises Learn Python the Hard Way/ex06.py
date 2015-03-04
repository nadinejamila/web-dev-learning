# We insert an integer and strings inside a string.
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"

# We insert multiple variables inside a string.
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# The use of %r prints out the raw data of the variable. 
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# The variable "hilarious" is still inserted 
#inside "joke_evaluation" even if it is inside a variable.
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# The plus sign concatenates two strings without a space.
print w + e