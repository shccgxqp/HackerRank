"""
Question : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
Difficul : tyEasy
Max Score : 5

"""

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    heigh = max(arr)
    arr.sort()
    arr.reverse()
    for i in arr:
        if i != heigh:
            print(i)
            break