'''
The array contains the student's test results. A value of True indicates that the student answered the question correctly, while a value of False indicates an incorrect answer.
 Write a program that prints information about the test results:

Number of questions:
Number of correct answers:
Number of incorrect answers:
Percentage of correct answers:'''
###
# Prints test statistics
#
test_results = [
   False, True, False, True, True,
   True, True, False, True, True,
   False, True, True, True, False
]

# calculates the number of test questions
question number = len(...)

# calculates the number of correct answers
correct_answers = 0
for answer in test_results:
   if ...:
      correct_answer = ...

# calculates the number of incorrect answers
...

# calculates the percentage of correct answers
...

print('TEST STATISTICS')
print('===============')
print('Number of questions:', ...)
print('Number of correct answers:', ...)
...
...