"""
Question : https://www.hackerrank.com/challenges/alphabet-rangoli/problem
Difficulty : Easy
Max Score : 20

"""
def print_rangoli(size):
    for i in range(1, size * 2):
        lst = []
        if i<=size:
            for j in range(i):
                lst.append(chr(96+ size-j))
            for k in range(i-1):
                lst.append(chr(96+ size- i+ 2+ k))
        else:
            for j in range(2* size- i):
                lst.append(chr(96+ size- j))
            for k in range(2* size- i- 1):
                lst.append(chr(96+ k+ i- size+ 2))
        print('-'.join(lst).center(size* 4-3,'-'))
