# the problem solved in this example is 
# https://www.hackerrank.com/challenges/three-month-preparation-kit-mini-max-sum/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-one

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    
    # where we store the lowest addition, notice that we add up the first four 
    # numbers as reference to when we find the other possible combinations
    lowest_addition = arr[1] + arr[2] + arr[3] + arr[4]
    
    # where we store the highest addition
    highest_addition = arr[1] + arr[2] + arr[3] + arr[4]
    
    # the idea here is that we need to find all of the possible combinations of additions between each number. to do this we are going to loop 4 times through=
    # the array as we need to find all of the combinations of 4 different numbers, every time we loop, we are going to add one to the loop so that we get all of the possible
    #combinations

    # we first loop through the array once
    for i in range(len(arr)):
        
        # we double loop through the arr starting from 1 after the previous index
        for s in range(i+1, len(arr)):
            
            # we triple loop starting from 1 after the previous index
            for x in range(s+1, len(arr)):
                
                # quadruple loop starting from 1 after the previous index
                for y in range(x+1, len(arr)):
                
                    # here we add all of the numbers
                    addition = arr[i] + arr[s] + arr[x] + arr[y]
                    
                    # if the addition is lower that the reference number then we declare it as the highest addition
                    if addition > highest_addition:
                        highest_addition = addition
                    
                    # if on the contrary it is lower, then we declare it as the lowest
                    if addition < lowest_addition:
                        lowest_addition = addition

    # in the end we should have exhausted all of the possible combinations of numbers and in par, found the max and min additions, now we just print them
    print(f'{lowest_addition} {highest_addition}')
        
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
