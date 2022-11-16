"""
Question : https://www.hackerrank.com/challenges/py-check-strict-superset/problem
Difficulty : Easy
Max Score : 10

Task :

Note :

"""

A = set(map(int, input().split()))
B = [set(map(int, input().split())) for i in range(int(input()))]

result = all([A.issuperset(b) and len(A) > len(b) for b in B])

print(result)
