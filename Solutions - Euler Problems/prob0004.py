"""
Largest palindrome product
Problem 4
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

Answer: 906609
"""


def is_palindrome(number):
    number = str(number)
    if number == number[::-1]:
        return True
    else:
        return False


def get_n_digit_factor(n):
    palindromes = []
    x = '9' * n
    x = int(x)
    y = x
    while len(str(x)) == 3:
        print 'X ---- ' + str(x)
        while len(str(y)) == 3:
            print str(y)
            if is_palindrome(x*y):
                palindromes.append(x*y)
                #return 'PALINDROME: ' + str(x*y) + ' = ' + str(x) + ' * ' + str(y) 
            y-=1
        x-=1
        y = 999
    return max(palindromes)

print get_n_digit_factor(3)
