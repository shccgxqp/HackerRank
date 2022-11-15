"""
Question : https://www.hackerrank.com/challenges/capitalize/problem
Difficulty : Easy
Max Score : 20
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    lst = s.split(' ')
    return ' '.join(list(map(lambda x: str.upper(x[0]) + x[1:] if len(x) >= 1 else x, lst))) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
