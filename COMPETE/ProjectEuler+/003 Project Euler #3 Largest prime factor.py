"""
Question : https://www.hackerrank.com/contests/projecteuler/challenges/euler003/problem

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""
#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    for i in range((n//2)+1,0,-1):
        for n in range(2,int(i/2)):
            if i%n ==0:
                break
        else:
            print(i)
            break