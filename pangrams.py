#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here

    # first we make the string all lowercase
    s = s.lower()
    
    letters_of_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l',
                        'm','n','o','p','q','r','s','t','u','v','w','x','y','z']

    # where we count the occurences of letters in the string (should be equal to 26 at the end for pangram)
    letter_count = 0
    
    for letter in letters_of_alphabet:
        if letter in s:
            letter_count += 1

    if letter_count == 26:
        return 'pangram'
    else:
        return 'not pangram'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
