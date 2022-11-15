"""

Question : https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem

If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""
#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    v3 = (n-1) // 3
    v5 = (n-1) // 5
    v15 = (n-1) // 15

    s3 = 3 * v3 * (1 + v3) // 2
    s5 = 5 * v5 * (1 + v5) // 2
    s15 = 15 * v15 * (1 + v15) // 2

    print((int)(s3 + s5 - s15))