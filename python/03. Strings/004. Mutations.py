"""
Question : https://www.hackerrank.com/challenges/whats-your-name/problem
Difficulty : Easy
Max Score : 10

"""

def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
    
    return  string

