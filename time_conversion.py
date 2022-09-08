# this is the solution for problem:
# https://www.hackerrank.com/challenges/three-month-preparation-kit-time-conversion/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-one

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    #print(s)

    # we check teh datetimes in am
    if 'AM' in s:
        # we remove the AM part
        s = s.replace('AM','')
        
        # we split the string with the delimiter toi separate the hour, minute and seconds
        new_time_list = s.split(':')
        
        # of the hour is above 12:
        if int(new_time_list[0]) >= 12:
            # we remove 12 from the first part so the hour
            new_time_list[0] = int(new_time_list[0])
            new_time_list[0] = f'0{new_time_list[0] - 12}'

        # now we construct the new string with the elements of the list
        separator = ':'
        new_string = separator.join(new_time_list)

    else:
        # we remove the PM part
        s = s.replace('PM','')

        # we split the string with the delimiter to separate the hour, minutes and seconds
        new_time_list = s.split(':')
        
        # we check if the hour is under 12 in that case we need to add 12 to it to adhere to military time
        if int(new_time_list[0]) < 12:
            new_time_list[0] = f'{int(new_time_list[0]) + 12}'
        
        # now we construct the new string with the elements of the list
        separator = ':'
        new_string = separator.join(new_time_list)
    
    return new_string


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()




