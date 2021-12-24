'''
Coin Flip Streaks
Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly
generated list of heads and tails. Your program breaks up the experiment into two parts: the first part
generates a list of randomly selected 'heads' and 'tails' values, and the second part checks if there is a streak
in it. Put all of this code in a loop that repeats the experiment 10,000 times so we can find out what
percentage of the coin flips contains a streak of six heads or tails in a row. As a hint, the function call
random.randint(0, 1) will return a 0 value 50% of the time and a 1 value the other 50% of the time.

You can start with the following template:
import random
numberOfStreaks = 0
for experimentNumber in range(10000):
# Code that creates a list of 100 'heads' or 'tails' values.
# Code that checks if there is a streak of 6 heads or tails in a row.
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
'''

import random
heads = 0
for i in range(1, 1001):
    if random.randint(0, 1) == 1:
        heads = heads + 1
    if i == 500:
        print('Halfway done!')
print('Heads came up ' + str(heads) + ' times.')
