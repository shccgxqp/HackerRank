"""
Question : https://www.hackerrank.com/challenges/list-comprehensions/problem
Difficulty : Easy
Max Score : 5

"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    x=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n]
    print(x)