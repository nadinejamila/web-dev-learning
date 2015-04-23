people = 30
cars = 40
trucks = 15

# This cheks if cars are more than people
if cars > people:
	print "We should take the cars."
# If the previous statement is not True, this statement is run.
elif cars < people:
	print "We should not take the cars."
# If the previous statement is not True, this statement is run. 
else:
	print "We can't decide."

if trucks > cars:
	print "That's too many trucks."
elif trucks < cars:
	print "Maybe we could take the trucks."
else: 
	print "We still can't decide."

if people > trucks:
	print "Alright, let's just take the trucks."
else:
	print "Fine, let's stay at home then."