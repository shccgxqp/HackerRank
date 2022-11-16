"""
Question : https://www.hackerrank.com/challenges/no-idea/problem
Difficulty : Medium
Max Score : 50

"""

nm = input()
arr = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

print(sum([(i in A) - (i in B) for i in arr]))
