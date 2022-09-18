# this is my solution to the problem mars exploration
# https://www.hackerrank.com/challenges/three-month-preparation-kit-mars-exploration/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-two

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):

    # the idea is that we want to iterate in steps of 3 through the strings,
    # so if we start at 0 then we will get 0,2,5,8 and so on. This means we can target 
    # the first word of every group of 3 words and match it to the SOS message

    # where we keep track of the altered letters
    other_letter_count = 0

    # we match the first S in SOS
    for i in range(0,len(s),3):
        # we check that the letter matches the first letter in SOS
        if s[i] != 'S':
            other_letter_count += 1

    # we match the second letter O in SOS, this time starting at the index 1
    for j in range(1, len(s), 3):
        # we check that the ltter matches with the second letter in SOS
        if s[j] != 'O':
            other_letter_count += 1

    # we match the last letter S in SOS, this time starting at the index 2
    for k in range(2,len(s), 3):
        # we check that the letter matches with the third letter in SOS
        if s[k] != 'S':
            other_letter_count += 1
        
    return other_letter_count
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
