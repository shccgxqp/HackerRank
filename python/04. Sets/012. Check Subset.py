"""
Question : https://www.hackerrank.com/challenges/py-check-subset/problem
Difficulty : Easy
Max Score : 10

Task :

Note :

"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for i in range(n):
    m = int(input())
    A = set(map(int, input().split()))
    k = int(input())
    B = set(map(int, input().split()))
    print(A.issubset(B))

