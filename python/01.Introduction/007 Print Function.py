"""
Question : https://www.hackerrank.com/challenges/python-print/problem
Difficul : tyEasy
Max Score : 5

"""

if __name__ == '__main__':
    n = int(input())
    list1 = [str(i) for i in range(1,n+1)]
    print(''.join(list1))
