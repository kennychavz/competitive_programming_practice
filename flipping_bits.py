#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import islice

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here
        
    # switching to bit

    # where we store the bit (starts with 0 everywhere)
    bit_count = ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']

    # we have to do a reverse for loop with a range of 32
    for i in range(31, -1, -1):

        # we check the result of the exponent of base 2 by the range (with 32 being the highest)
        exponent_result = 2 ** i

        # we substract the result from the initial number and if the result is under 0, we skip to the next
        if n - exponent_result < 0:
            continue

        # if the substraction is not under 0 then we swittch its corresponding bit to 1 
        bit_count[31-i] = '1'

        # we also remove the exponent_result from the initial integer we are manipulating
        n = n - exponent_result


    # we need to switch the bits to that those that are 1 become 0 and vice versa
    for i in range(len(bit_count)):
        if bit_count[i] == '1':
            bit_count[i] = '0'
        elif bit_count[i] == '0':
            bit_count[i] = '1'


    # we concatenate the list together
    converted_bit = ''
    for element in bit_count:
        converted_bit += element

    # now we need to switch back to base 10

    # we keep the base 10 result here where we add the numbers from the bit number
    base_10_result = 0

    # we do a loop through the elements in bit_count
    for index in range(len(bit_count)):
        # if the number is 1 it means that it it a multiple of 2 that we need to add to the base_10_result
        if bit_count[index] == '1':
            # this number to be added is based on 2 exponential the index of the list element (which is reversed because
            # we read bit number from right to left)
            base_10_result += 2 ** (32 - index - 1)

    # we return the converted bit
    return base_10_result


# this is where we treat the input
for i in range(int(input())):
    print(flippingBits(int(input())))