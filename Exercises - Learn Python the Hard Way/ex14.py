#This imports argv from the sys module
from sys import argv

# This unpacks the arguments entered before the script is run.
# e.g. python ex14.py nadine
script, user_name = argv
prompt = '>>> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer  =raw_input(prompt)

# This prints out a multiline string which displays the data input from the user.
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)