"""
Question : https://www.hackerrank.com/challenges/symmetric-difference/problem
Difficulty : Easy
Max Score : 10

"""

a = input()
seta = set(map(int,input().split()))
b = input()
setb = set(map(int,input().split()))

setc= sorted((seta.difference(setb)).union(setb.difference(seta)))
for x in setc:
    print(x)
