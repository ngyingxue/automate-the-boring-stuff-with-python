'''
Date Detection

Write a regular expression that can detect dates in the DD/MM/YYYY format. Assume that the days range
from 01 to 31, the months range from 01 to 12, and the years range from 1000 to 2999. Note that if the day
or month is a single digit, it’ll have a leading zero.
The regular expression doesn’t have to detect correct days for each month or for leap years; it will accept
nonexistent dates like 31/02/2020 or 31/04/2021. Then store these strings into variables named month, day, and
year, and write additional code that can detect if it is a valid date. April, June, September, and November
have 30 days, February has 28 days, and the rest of the months have 31 days. February has 29 days in leap
years. Leap years are every year evenly divisible by 4, except for years evenly divisible by 100, unless the year
is also evenly divisible by 400. Note how this calculation makes it impossible to make a reasonably sized
regular expression that can detect a valid date.
'''

import re

dateDetection = re.compile(r'''
    (0[1-9]|1[0-9]|2[0-9]|3[0-1]) # Day
    / # Slash
    (0[1-9]|1[0-2]) # Month
    / # Slash
    (1[0-9]{3}|2[0-9]{3}) # Year
    ''',re.VERBOSE)

dates = dateDetection.findall('this is a date 29/02/2000')

day = []
month = []
year = []

for date in range(len(dates)):
    day.append(dates[date][0])
    month.append(dates[date][1])
    year.append(dates[date][2])

if day == [] or month == [] or year == []:
    print('No valid date found.')

for i in range(len(day)):
    invalid_indicator = 0
    if month[i] in ['04','06','09','11'] and day[i] == '31':
        invalid_indicator += 1
    if int(year[i]) % 4 == 0: # leap year
        if int(year[i]) % 100 == 0: # not leap year
            if int(year[i]) % 400 != 0: # not leap year
                if month[i] == '02' and day[i] == '29':
                    invalid_indicator += 1
    if int(year[i]) % 4 != 0: # not leap year
        if month[i] == '02' and day[i] == '29':
            invalid_indicator += 1
    if month[i] == '02'  and day[i] in ['30', '31']:
        invalid_indicator += 1
    if invalid_indicator != 0:
        print(day[i] + '/' + month[i] + '/' + year[i] + ' is an invalid date')
    if invalid_indicator == 0:
        print(day[i] + '/' + month[i] + '/' + year[i] + ' is a valid date')
