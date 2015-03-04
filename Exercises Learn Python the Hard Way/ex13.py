
# We add the argv feature that would allow us to input arguments to the script before it is run.
from sys import argv

# This line takes in the items typed in by the user before running the script.
# e.g. python <filename>.py <first> <second> <third>
script, first, second, third = argv

# We ask for more input from the user while the script is running.
fourth = raw_input("What's the fourth variable?: ")
fifth = raw_input("What's the fifth variable?: ")

# We print out all the user input.
print "The script is called: ", script
print "Your first variable is: ", first
print "Your second variable is: ", second
print "Your third variable is: ", third
print "Your fourth variable is: ", fourth
print "Your fifth variable is: ", fifth
