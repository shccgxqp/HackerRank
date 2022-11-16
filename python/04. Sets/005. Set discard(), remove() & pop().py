"""
Question : https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
Difficulty : Easy  
Max Score : 10

Task :

Note :

"""

n = int(input())
s = set(map(int,input().split()))
m=int(input())
for i in range(m):
    data=input().split()
    if data[0]=='remove':
            s.remove(int(data[1]))
    elif data[0]=='pop':
            s.pop()
    elif data[0]=='discard':
            s.discard(int(data[1]))
if len(s)==0:
        print (0)
else: 
        print(sum(s))