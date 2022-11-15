"""
Question : https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true
Difficul : tyEasy
Max Score : 5

"""
#pypy3


if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    print(hash(integer_list))
