# this is the solution to problem
# https://www.hackerrank.com/challenges/three-month-preparation-kit-grading/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-two

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here

    # we loop through the grades
    for index in range(len(grades)):

        # if the result is less than 38 we just skip
        if grades[index] < 38:
            continue

        # if the grade is not divised by 5
        if grades[index] % 5 == 0:
            continue

        # we check the remainder
        remainder = grades[index] % 5

        # if the remainder is
        if remainder > 2:
            grades[index] = grades[index] + (5-remainder)

    return grades

grades = [4,73,67,38,33]
print(gradingStudents(grades))


