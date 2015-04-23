############
# KEYWORDS #
############


# and
if True and False == False:
	print "True!"

# with & as
with X as Y:
	pass

# assert - ensure that something is True
assert False, "Error"

# while & break
while True:
	break

# class
class Person(object):
	pass

# continue
while True:
	continue

# def
def X():
	pass

#del - delete from dictionary
del X[Y]

# if, elif & else
if True: 
	X
elif True:
	Y
else:
	X

# try, except & finally
try: 
	pass
except ValueError, e:
	print e
finally:
	pass

# exec - run a string as Python
exec 'print "hello"'

# global
global X

# import
import os

# in
for X in Y:
	pass
x in [x] == True

# is
l is l == True

# lambda - create a short anonymous function
s = lambda y: y ** y
s(3)

# not
not True == False

# or
True or False == True

# pass
def empty():
	pass

# print
print 'this string'

# raise
raise ValueError("No")

# return
def X():
	return Y

# yield - pause here and return to caller
def X():
	yield Y
X().next()