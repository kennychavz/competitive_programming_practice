# this is my solution to
# https://www.hackerrank.com/challenges/three-month-preparation-kit-counting-valleys/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-two


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
   
    # everytime the step count goes below 0 and comes back to 0 this counts as one valley

    # where we keep count of the altitude
    step_count = 0

    # where we keep track of the numbers of valleys
    valley_count = 0

    # we loop through the characters
    for char in path:

        print(f'the step count is {step_count}')

        # we check for uphill steps when the step_count is currently equal to -1
        if char == 'U':

            if step_count == -1:

                print(f'we are going to reach sea level')
                
                # we addd one to the valley counter
                valley_count += 1

            # we add one step to the step counter
            step_count += 1
        
        # else, if the step is a downhill step then we subtract one from the step counter
        elif char == 'D':

            step_count -= 1

    # we return the number of valleys to the user
    return valley_count

int_steps = input()
string_path = input()

# we call the method
print(countingValleys(int_steps, string_path))