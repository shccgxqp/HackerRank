"""
Question : https://www.hackerrank.com/challenges/py-the-captains-room/problem
Difficulty : Easy
Max Score : 10

Task :

Note :

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
set_ = list(map(int, input().split()))
count = {}
for i in set_:
    if i in count.keys():
        count[i] = count[i] + 1
    else:
        count[i] = 1
for i in count.keys():
    if count[i] == 1:
        print(i)