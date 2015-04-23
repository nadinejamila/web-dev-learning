from sys import argv

script, input_file = argv

def print_all(f):
	# This prints out the contents of a file object.
    print f.read()

def rewind(f):
	# seek(0) moves the file to the 0 byte (first byte) in the file.
    # Other values are 1 which means seek relative to the current position and 2 means seek relative to the file's end.
    f.seek(0)

def print_a_line(line_count, f):
	# Readline returns the current line and goes to the next line.
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."


rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)