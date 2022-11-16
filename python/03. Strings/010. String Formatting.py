"""
Question : https://www.hackerrank.com/challenges/python-string-formatting/problem
Difficulty : Easy
Max Score : 10
"""

def print_formatted(number):
    # your code goes here
    max_width = len(bin(number)[2:])
    
    for x in range(1, number + 1):
        print(str(x).rjust(max_width, " "), end=" ")
        print(oct(x)[2:].rjust(max_width, " "), end=" ")
        print(hex(x)[2:].upper().rjust(max_width, " "), end=" ")
        print(bin(x)[2:].rjust(max_width, " "))
        

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)