# this is my solution for problem
# https://www.hackerrank.com/challenges/three-month-preparation-kit-diagonal-difference/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-two

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here 

    left_to_right_diagonal = 0
    right_to_left_diagonal = 0
    
    # we will double loop through the matrix inside of the array to find all possible combinations of indexes
    for i in range(len(arr)):
        for j in range(len(arr)):

            # for left to right diagonal we will just add the numbers that have the same i and j indexes
            if i == j:

                # we add the number to the left_to_right_diagonal sum
                left_to_right_diagonal += arr[i][j]

    # for the right to left diagonal we will loop through each row and reverse the order of the rows
    for index in range(len(arr)):
        arr[index].reverse()
    
    # we follow the same double loop as previously done with the new reversed matrix
    for i in range(len(arr)):
        for j in range(len(arr)):

            # for left to right diagonal we will just add the numbers that have the same i and j indexes
            if i == j:

                # we add the number to the left_to_right_diagonal sum
                right_to_left_diagonal += arr[i][j]

    # we return the absolute difference between both
    return abs(right_to_left_diagonal - left_to_right_diagonal)

# test case
# test_case = [
#     [1,2,3],
#     [4,5,6],
#     [9,8,9]
# ]
# print(diagonalDifference(test_case))