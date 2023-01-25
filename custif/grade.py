#!/usr/bin/env python3

""" if, elif,else grade project 
A program that prompts a user for a numeric score, then returns the letter grade associated with that score.
A (100 to 90)
B (89 to 80)
C (79 to 70)
D (69 to 60)
F (59 and below)"""
"""
Traceback (most recent call last):
  File "/home/student/mycode/custif/grade.py", line 23, in <module>
    print("C grade " + rating)
TypeError: can only concatenate str (not "float") to str"""

# wrap connection in a float() to accept decimals as numbers
rating = float(input("What is your current rating (0-100)?"))

# if input value was higher or equal to 25
if rating >= 90:
#    message = message + 'A grade'
    print("A grade " + rating)
elif rating >= 80:
#    message = message + 'B grade'
    print("B grade " + rating)
elif rating  >= 70:
#    message = message + 'C grade'
    print("C grade " + rating)
elif rating  >= 60:
#    message = message + 'D grade'
    print("D grade " + rating)
else:
#    message = message + 'F'
     print("F grade " + rating)
