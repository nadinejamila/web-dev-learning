# Notes on Learn Python the Hard Way
These are my personal notes for the important things not to be missed out from the book.

## Data Output
#### The print statement
We display objects such as strings and integers with `print`.
```python
print "Hello World!"
```

#### Comments
Anything after `#` (a.k.a. octothorpe or pound key) is ignored by python.
```python
# A comment, this is so you can read your program later.
print "Hello World!"
```

#### Strings
A string is a bit of text you want to display using `'` or `"`, and `'''` or `"""` for multi-line strings.
```python
print 'I am a string.'
print "I can also have double quotes around me."
print """
I am a string
that span across
multiple lines.
"""
```

#### Numbers and Math
Math operations in python follow the PEMDAS rule. These are the symbols used:
- `+` plus for addition
- `-` minus for substraction
- `/` slash for division
- `*` asterisk for multiplication
- `%` percent as modulus
- `<` less-than
- `>` greater-than
- `<=` less-than-equal
- `>=` greater-than-equal

```python
# This will give us the sum of 3 and 2
print 3 + 2
```

#### Variables and Names
A variable is a name for something, similar to how my name "Nadine" is a name for, "The girl who wrote these notes."
We use `=` to assign items into variables and `_` as space if need be.
```python
my_name = 'Nadine'
my_current_age = 23
```

#### Variables and String formatting
Strings may contain the format characters such as `%s`, `%d`, and `%r` for printing the contents of our variable.
- `%d` - for printing numeric values
- `%r` - for printing out the actual contents of the variable for debugging purposes

```python
my_name = 'Nadine
my_current_age = 23
height = '5\'7"'
print "Hi, my name is %s and I am %d years old. I stand %r tall." % (my_name, my_current_age, height)
```
will give us...
```
> Hi, my name is Nadine and I am 23 years old. I stand '5\'7"' tall.
```

#### Escape Sequences
There are various "escape sequences" available for different characters you might want use for different purposes.
```python
"I am 6'2\" tall."  # escape double-quote inside string
'I am 6\'2" tall.'  # escape single-quote inside string
```
Commonly used ones:
- `\\` - show backslash
- `\'` - show single-quote
- `\"` - show double-quote
- `\n` - line break
- `\r` - return carriage
- `\t` - tab

## Data Input

#### Method 1: using  `raw_input`
`raw_input()` lets the user enter data **WHILE** the script is running, like this.
This prompts the user with "What is your name?" and puts the result into the variable `your_name`. This is how you ask someone a question and get the answer.
```python
your_name = raw_input("What is your name?")
print "Hi %s. It's nice to meet you." % your_name
```

#### Method 2: using `argv`
`argv` lets the user enter data **BEFORE** the script is run, like this:
```
$ python my_script.py Nadine Nads
```
`argv` holds the arguments (i.e. "Nadine" and "Nads") we passed to our Python script when we ran it.
```python
from sys import argv # We use the sys module for this feature

# This "unpacks" argv so that, rather than holding all the arguments, it gets assigned to variables we can work with.
script, your_name, your_nickname = argv

print "The script is called:", script
print "My name is %s, but you can call me %s." % (name, nickname)
```


## Working with Files

#### Reading Files
What we want to do is "open" a file in our script and print it out.
- `open()` - preferred way to open files, returns a file object
- `read()` - gets the contents of the file
```python
from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()
```

#### Reading & Writing Files

Important commands:
- `close()` - closes the file. LIke `File-> Save..` in an editor
- `read()` - reads the contents of the file, usually assigned to a variable
- `readline()` - reads just one line of a text file
- `truncate()` - empties the file
- `write(stuff)` - writes "stuff" to the file
This script truncates a file given by the user, and replaces its contents with the new input from the user.
```python
from sys import argv

script, filename = argv

print "Would you like to erase %r?" % filename
print "If yes, hit RETURN. If no, hit CTRL-C (^C)."
raw_input("?")

# We open the file.
target = open(filename, 'w')

# The file is emptied.
target.truncate()

print "Let's make a wishlist. You can have 3 wishes."
line1 = raw_input("wish 1: ")
line2 = raw_input("wish 2: ")
line3 = raw_input("wish 3: ")

print "I'm going to write these in the wishlist."
# This writes the user input into the open file.
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

# Finally, we close the file.
target.close()
```
reminders: 
- `open(filename, 'w')` is used for writing files. An existing file with the same name will be **erased**.
- **Always** close a file after opening them. Open files consume system resources, and depending on the file mode, other programs may not be able to access them. 


## Functions
Functions do 3 things:
- They name pieces of code.
- They take arguments (similar to argv).
- They let you make your own "mini-scripts" or "tiny commands."

#### Creating a function
`def` stands for "define". Function names may contain letters, numbers, and underscores, but they can't start with a number.
```python
def function_name(arg1, arg2):
    print "We can use the arguments %r and %r inside the function." % (arg1, arg2)
```

#### Functions and Variables
The variables in your function are not connected to the variables in your script. 
Below are different ways we can give our function the values it needs to print them.
```python
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers

# We can just give the function numbers directly.
cheese_and_crackers(20, 30)

# OR, we can use variables from our script.
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# We can even do math inside too.
cheese_and_crackers(10 + 20, 5 + 6)

# And we can combine the two, variables and math.
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
```

#### Functions and Files
```python
def print_a_line(f):
	print f.readline()
	
def rewind(f):
	f.seek(0)
```
- `readline()` returns the `\n` that's in the file at the end of that line. The file `f` is responsible for maintaining the current position in the file after each `readline()`.
- `seek(0)` moves the file to the 0 byte (first byte) in the file
- `seek(1)` moves the file relative to the current position
- `seek(2)` moves the file to the file's end

#### Function's Return Value
We use `return` in our function to get a result from that function, and set them into variables to be used later on. 
```python
def get_the_sum(num1, num2):
    return num1 + num2

the_sum = get_the_sum(1, 2) #The function returned something
print the_sum
```


## Logic & Control Flow

#### Truth terms
- `and`
- `or`
- `not`
- `!=` (not equal)
- `==` (equal)
- `>=` (greater than or equal)
- `<=` (less than or equal)
- `True`
- `False`

#### `if` Statements
- An `if` statement creates a "branch" in the code. Meaning, if the boolean expression after `if` is True, the code under it, i.e. the indented block, is run.
- An `elif` statement, also knows as "else if", creates another branch of code as we add another boolean expression.
- An `else` statement is run when all previous statements are not True.
```python
if False:
    print "This does not get printed out."
elif False:
    print "This does not get print out."
elif True:
    print "This gets printed out."
else:
    print "This does not get print out."
```
Python only runs the first block it determines to be True, so it will run on the third one, and stop after that.

#### `for` Loop
`for` loops allow us to do repetitive things very quickly.
The `range()` gives us a list of numbers which is very useful for our `for` loops. However, this function only does numbers from the first to the last, not including the last.
```python
for i in range(0, 6):
    print i
    # This only prints out the numbers from 0 to 5
```
#### `while` Loop
A `while` loop will keep executing the code block under it as long as a boolean expression is True. It runs until the expression is False.
###### Rules on `while` loops
- use sparingly
- make sure it becomes `False` at some point
- print out your test variable at the top & nottom of the loop to see that it's doing
```python
i = 0
while i < 3:
   print "from", i
   i = i + 1
   print "to", i
```

## Key Words

- `as` - rename an item

    ```python
    import random as rnd

    for i in range(10):
      print rnd.randint(1, 10)
    ```
- `assert` - ensure that something is True
    
    ```python
    assert False, "Error"
    ```
- `exec` - run a string as Python

    ```python
    exec 'print "hello"'
    ```
- `lambda` - create a short anonymous function

    ```python
    s = lambda y: y ** y
    s(3)
    ```
- `yield` - pause here and return to caller

    ```python
    def X():
      yield Y
    X().next()
    ```
[see more keywords here](http://learnpythonthehardway.org/book/ex37.html)

## Data Structures

#### Lists
A list is for an *ordered* list of items such as strings, numbers, objects, another list, etc., possibly of different types.
###### List operations
- `append(object)`
- `count(value)`
- `extend(iterable)`
- `index(value)`
- `insert(index)`
- `pop([index])`
- `remove(value)`
- `reverse()`
- `sort()`

###### Accessing elements
`list[index]` wherein index is the nth position of the element, starting from zero.

#### Dictionaries
A dictionary (or dict) is for matching some items (called "keys") to other items (called "values").
```python
# create a dictionary
args = {}

# add items
args['name'] = 'Nadine'
args['age'] = 23

# get an item
name = args.get('name', 'Does Not Exist')

# delete items
del args['age']

# show contents as a dictionary
print args
# This would show {'name': 'Nadine, 'age': 23}

# show key value pairs as tuple
print args.items()
```

## Modules
A module as a specialized dictionary that can store Python code (e.g. variables and functions) so you can access it with the `.` operator. When you import a module there is only **one** for the entire program.
```python
#This goes to my_module.py

name = 'Nadine'

def whoami(name):
    print "Hi, I'm", name
```
```python
import my_module

name = my_module.name
my_module.whoami(name)
# This prints Nadine
my_module.woami('Camille')
# This prints Camille
```
## Classes
 A class is a way to take a grouping of functions and data and place them inside a container so you can access them with the `.` operator. 
 
 Unlike modules, classess can be used to craft **many** of these groupings (called *instantiation*), and each one won't interfere with each other.
 ```python
class Person(object):

    def __init__(self, name):
        self.name = name

    def introduction(self):
        print "Hi, my name is", self.name
        
# instantiate a Person
me = Person('Nadine')
me.introduce()
# This prints out 'Hi, my name is Nadine'

# instantiate another Person
friend = Person('Camille')
friend.introduce()
# This prints out 'Hi, my name is Camille'
 ```

## Object-Oriented Programming (OOP) Concepts
##### Keywords
- class
- object
- instance
- def
- self
- inheritance
- composition
- attribute
- is-a
- has-a

[description of terms here](http://learnpythonthehardway.org/book/ex41.html)

#### Inheritance (is-a)
Inheritance is used to indicate that one class will get most or all of its features from a parent class. 
###### 3 ways:
- Implicit Inheritance
- Override Explicitly
- Alter Before or After
	- `super()` runs the method of a parent class
```python
class Parent(object):

	def override(self):
		print "PARENT override()"

	def implicit(self):
		print "PARENT implicit()"

	def altered(self):
		print "PARENT altered()"


class Child(Parent):

	def override(self):
		# This function overrides the baseclass' function
		print "CHILD override()"

	def altered(self):
		# This function alters the baseclass' function
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered()
		print "CHILD, AFTER PARENT altered()"

```
The most common use of `super()` is actually in `__init__` functions in base classes.

```python
class Child(Parent):

    def __init__(self, stuff):
        self.stuff = stuff
        super(Child, self).__init__()
```

###### Multiple Inheritance
Multiple inheritance is when you define a class that inherits from one or more classes.

```python
class SuperFun(Child, BadStuff):
    pass
```

#### Composition (has-a)
Another way to get another class' features is to just use them, rather than rely on implicit inheritance. 

```python
class Other(object):

    def override(self):
        print "OTHER override()"

    def implicit(self):
        print "OTHER implicit()"

    def altered(self):
        print "OTHER altered()"

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE OTHER altered()"
        self.other.altered()
        print "CHILD, AFTER OTHER altered()"

son = Child()

son.implicit()
son.override()
son.altered()
```

#### Inheritance vs Composition

###### Guidelines
- **Avoid multiple inheritance** if you can. If not, then know the class hierarchy and spend time finding where everything is coming from.
- **Use composition** to package code into modules that are used in many different unrelated places and situations.
- Use inheritance only when there are clearly related reusable pieces of code that fit under a single common concept or if you have to because of something you're using.

## Project Setup

#### Suggested Python packages
- pip from http://pypi.python.org/pypi/pip
- distribute from http://pypi.python.org/pypi/distribute
- nose from http://pypi.python.org/pypi/nose/
- virtualenv from http://pypi.python.org/pypi/virtualenv

#### Installing your own Python package
###### The `setup.py` file:
To install our project, we need to create a `setup.py` file.
```
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'My Name',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
```
To install the package:
```
python setup.py install
```

#### Sample Project Structure
The basic directorys structure should look like this:
```
skeleton/
     NAME/
         __init__.py
     bin/
     docs/
     setup.py
     tests/
         NAME_tests.py
         __init__.py
```
where `skeleton` is the name of the project and `NAME` is the name of the python module.

###### Putting a script in the bin directory
1. Create the script.
```
# bin/my_script

#!/usr/bin/env python

import my_module
my_module.my_pythonfile.my_function()
```
2. Add the script in `setup.py`.
```
config = {
    ...
    'scripts': ['bin/my_script'],
    ...
}
```

## Automated Testing

1. Install `nose`.

	```
	$ pip install nose
	```
2. Create a `tests` folder in the root folder.
3. For each python file in the root, create a `<file_name>_tests.py`.

	```
	my_project\
	       setup.py
	       my_module\
		      __init__.py
		      first_file.py
		      second_file.py
	       tests\
		      first_file_tests.py
		      second_file_tests.py
	```
4. Create tests inside the test file, like so:

	```python
	# first_file_tests.py
	
	from nose.tools import *
	from first_file import Room
	
	def test_room():
	    gold = Room("GoldRoom")
	    assert_equal(gold.name, "GoldRoom")
	```
5. Run the test in the root folder, like so:

	```
	$ nosetests
	```
	
## Errors & Exceptions

#### Raising an error
```
def parse_verb(word_list):
    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")
```

####  Using `try` & `except`
```
while True:
     try:
         x = int(raw_input("Please enter a number: "))
         break
     except ValueError:
         print "Oops!  That was no valid number.  Try again..."
```


