'''
Sandwich Maker

Write a program that asks users for their sandwich preferences. The program should use PyInputPlus to ensure that they enter valid input, such as:

Using inputMenu() for a bread type: wheat, white, or sourdough.
Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
Using inputYesNo() to ask if they want cheese.

If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or mozzarella.

Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
Using inputInt() to ask how many sandwiches they want. Make sure this number is 1 or more.

Come up with prices for each of these options, and have your program display a total cost after the user enters their selection.
'''

import pyinputplus as pyip

bread = pyip.inputMenu(['wheat','white','sourdough'], prompt='What bread type do you want?\n')
protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], prompt='what protein type do you want?\n')
cheese = pyip.inputYesNo('Do you want cheese?\n')

if cheese == 'yes':
    cheeseType = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], prompt='what type of cheese do you want?\n')

mayo = pyip.inputYesNo('Do you want mayo?\n')
mustard = pyip.inputYesNo('Do you want mustard?\n')
lettuce = pyip.inputYesNo('Do you want lettuce?\n')
tomato = pyip.inputYesNo('Do you want tomato?\n')

number = pyip.inputInt('How many sandwiches do you want?\n')

totalCost = 0

# bread cost
if bread == 'wheat':
    totalCost += 1
if bread == 'white':
    totalCost += 2
if bread == 'sourdough':
    totalCost += 3

# protein cost
if protein == 'chicken':
    totalCost += 5
if protein == 'turkey':
    totalCost += 6
if protein == 'ham':
    totalCost += 7
if protein == 'tofu':
    totalCost += 4

# cheese cost
if cheeseType == 'cheddar':
    totalCost += 2
if cheeseType == 'Swiss':
    totalCost += 2.5
if cheeseType == 'mozzarella':
    totalCost += 3

# other condiments
if mayo == 'yes':
    totalCost += 0.5
if mustard == 'yes':
    totalCost += 1.5
if lettuce == 'yes':
    totalCost += 2.5
if tomato == 'yes':
    totalCost += 3.5

totalSandwichCost = totalCost*number

print('The total sandwich cost is $'+ str(totalSandwichCost))
