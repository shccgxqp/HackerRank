"""
Question : https://www.hackerrank.com/challenges/find-a-string/problem
Difficulty : Easy
Max Score : 10

"""

def count_substring(string, sub_string):
    count =0
    for i in range(len(string)):
        print(i,string[i:i+len(sub_string)], )
        if sub_string in string[i:i+len(sub_string)] :
            count +=1
    return count
count = count_substring('ABCDCDC', 'CDC')
print(count)