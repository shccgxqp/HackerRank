"""
Question : https://www.hackerrank.com/challenges/designer-door-mat/problem
Difficulty : Easy
Max Score : 10

    Size: 7 x 21 -> n x m
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = [int(x) for x in input().split()]
ptrn = ".|."
for i in range(1,n,2):
    print((ptrn*i).center(m, "-"))
    
print("WELCOME".center(m, "-"))

for i in range(n-2,0,-2):
    print((ptrn*i).center(m, "-"))