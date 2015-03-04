# The '=' sign assigns the following string/integers to a variable.
my_name = 'Nadine Jamila'
my_age = 23
my_height = 67 # inches
my_weight = 115 # lbs
my_eyes = 'Very dark brown'
my_hair = 'Dark Brown'

# %s or %d are used to insert a string or decimal in a string, respectively.
print "Let's talk about %s." % my_name
print "She's %d inches tall." % my_height
print "She's %d points heavy." % my_weight

# Parentheses and commas are used to insert multiple variables into one line of string.
print "She's got %s eyes and %s hair." % (my_eyes, my_hair)

# We can insert operations directly into string and the answer will be printed.
print "If i add %d, %d, and %d I get %d." % (
	my_age, my_height, my_weight, my_age + my_height + my_weight)

height_in_cm = my_height  * 2.54
weight_in_kg = my_weight * 0.453592

# This gives us floating point numbers as answers.
print "Her height in cm is %f." % height_in_cm
print "Her weight in kg is %f." % weight_in_kg
