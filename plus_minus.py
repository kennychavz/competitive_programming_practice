# this is the solution to problem:
# https://www.hackerrank.com/challenges/three-month-preparation-kit-plus-minus/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-one


#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    
    # we store the positive values here
    positive_values = []
    
    # we store the negative values here
    negative_values = []
    
    # we store the neutral values here
    neutral_values = []
    
    # we loop through the elements in the array
    for element in arr:
        
        # if the element is positiviepositive values
        if element > 0:
            positive_values.append(element)
            
        # negative values
        if element < 0:
            negative_values.append(element)
            
        # neutral values
        if element == 0:
            neutral_values.append(element)
            
    # ratio of positive values
    print(round(len(positive_values)/len(arr), 6))
    
    # ratio of negative values
    print(round(len(negative_values)/len(arr), 6))
    
    # ratio of neutral values
    print(round(len(neutral_values)/len(arr), 6))
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
