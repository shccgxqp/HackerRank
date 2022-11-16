"""
Question : https://www.hackerrank.com/challenges/py-set-add/problem
Difficulty : Easy  
Max Score : 10

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
set1 =set()

for i in range(int(n)):
    x = input()
    set1.add(x)
else:
    print(len(set1))
