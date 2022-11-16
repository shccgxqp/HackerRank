"""
Question : https://www.hackerrank.com/challenges/py-set-mutations/problem
Difficulty : Easy
Max Score : 10

Task :

Note :

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

input() 
a = set(map(int, input().split()))

for i in range(int(input())):
    command = str(input().split()[0])
    s = set(map(int, input().split()))
    eval(f"a.{command}({s})")
    
print(sum(a))
