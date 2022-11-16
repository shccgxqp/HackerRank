"""
Question : https://www.hackerrank.com/challenges/py-set-union/problem
Difficulty : Easy
Max Score : 10

Task :

Note :

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
a = input()
seta = set(map(int,input().split()))
b = input()
setb = set(map(int,input().split()))
print(len(seta.union(setb)))


