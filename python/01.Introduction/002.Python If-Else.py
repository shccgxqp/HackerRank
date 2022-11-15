"""
Question : https://www.hackerrank.com/challenges/py-if-else/problem

"""
if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 == 1 or (n>5 and n<21) :
        print('Weird')

    else :
        print('Not Weird')
