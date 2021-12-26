'''
Write Your Own Multiplication Quiz

To see how much PyInputPlus is doing for you, try re-creating the multiplication quiz project on your own without importing it. This
program will prompt the user with 10 multiplication questions, ranging from 0 × 0 to 9 × 9. You’ll need to implement the following features:

If the user enters the correct answer, the program displays “Correct!” for 1 second and moves on to the next question.
The user gets three tries to enter the correct answer before the program moves on to the next question.
Eight seconds after first displaying the question, the question is marked as incorrect even if the user enters the correct answer after
the 8-second limit.
'''

import pyinputplus as pyip
import random, time

numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(1, numberOfQuestions+1):
    # Pick two random numbers:renum1 = random.randint(0, 9)
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)

    try:
        # Right answers are handled by allowRegexes.
        # Wrong answers are handlded by blockRegexes, with a custom message.
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],
                                blockRegexes=[('.*', 'Incorrect!')],
                                timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        # This block runs if no exceptions were raised in the try block.
        print('Correct!')
        correctAnswers += 1

    time.sleep(1) # Brief pause to let user see the result.
print('Score: %s / %s' % (correctAnswers, numberOfQuestions))
