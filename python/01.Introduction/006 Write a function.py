"""
Question : https://www.hackerrank.com/challenges/write-a-function/problem
Difficulty : Medium
Max Score : 10

"""
def is_leap(year):
    leap = False
    
    if year % 100 ==0 and year % 400 != 0:
        return leap
    if year % 4==0 :
        return True
    
    return leap
