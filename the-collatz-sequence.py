''' 
The Collatz Sequence
Write a function named collatz() that has one parameter named number. If number
is even, then collatz() should print number // 2 and return this value. If number is
odd, then collatz() should print and return 3 * number + 1.
Then write a program that lets the user type in an integer and that keeps
calling collatz() on that number until the function returns the value 1.

Remember to convert the return value from input() to an integer with the
int() function; otherwise, it will be a string value.
Hint: An integer number is even if number % 2 == 0, and it’s odd if number % 2 == 1.

Input Validation
Add try and except statements to the previous project to detect whether the user
types in a noninteger string. Normally, the int() function will raise a ValueError
error if it is passed a noninteger string, as in int('puppy'). In the except clause,
print a message to the user saying they must enter an integer.
'''


def collatz(number):
    global value
    if number % 2 == 0:
        print(number//2)
        value = number // 2
    elif number % 2 == 1:
        print(3*number+1)
        value = 3*number+1


print('Enter number:', end = '\n')
#while True:
try:
    value = int(input())
    while True:
        collatz(value)
        if value == 1:
            break
except ValueError:
    print('You must enter an integer')
