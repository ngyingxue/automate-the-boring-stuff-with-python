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
