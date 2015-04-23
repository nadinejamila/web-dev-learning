
# %r enables us to print several types of variables, be it integer, string, or boolean values.
# Unlike %s or %d which only lets us print strings and numberic values, respectively.

# This 'formatter' string can take in variables and format how we would want to present those variables.
# This time, we would present them as a plain string with a blankspace separating them.
formatter = '%r %r %r %r'

# We can insert integers inside the 'formatter' string.
print formatter % (1, 2, 3, 4)

# We can insert strings inside the 'formatter' string
print formatter % ('one', 'two', 'three', 'four')

# We can insert boolean values in the 'formatter' string
print formatter % (True, False, False, True)

# We can insert strings inside the 'formatter' string, with formatter both as a plain string and as THE formatter.
print formatter % (formatter, formatter, formatter, formatter)

# We insert strings inside the 'formatter' string. 
# It is possible to have new lines for each tuple item.
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)