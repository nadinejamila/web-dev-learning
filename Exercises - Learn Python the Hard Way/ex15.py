
# Remember to import argv from the sys module
from sys import argv

# We use argv to get the filename from the user before the script is run
script, filename = argv

# open() returns a file object with the filename specified by the user, and keeps it inside a variable.
# This is the preferred way to open a file.  
txt = open(filename)

print "Here's your file %r: " % filename

# We get the contents of the file using the read() function.
print txt.read()


# Here is another way to do the script above, but using raw_input() this time.
print "Type the filename again:"
file_again = raw_input("> ")
txt_again = open(file_again)
print txt_again.read()