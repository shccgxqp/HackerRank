"""
Question : https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
Difficulty : Easy
Max Score : 10

Task :

Note :

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
eng_news = list(map(int, input().split(' ')))
b = int(input())
french_news = list(map(int,input().split()))

result = set(eng_news).intersection(set(french_news))
print(len(result))
