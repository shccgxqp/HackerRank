"""
Question : https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
Difficulty : Easy
Max Score : 10

Task :

Note :

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
n=input()
a=set(input().split())
m=input()
b=set(input().split())

print(len(a^b))
