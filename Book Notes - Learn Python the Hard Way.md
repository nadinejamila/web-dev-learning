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

## Data Structures

#### Lists
Lists may contain items such as strings, numbers, objects, another list, etc., possibly of different types.
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

## Key Words

- `as` - We use the `as` keyword if we want to give a module a different alias.
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