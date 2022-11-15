"""
Question : https://www.hackerrank.com/challenges/finding-the-percentage/problem
Difficul : tyEasy
Max Score : 5

"""

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = student_marks[input()]
print('%.2f' % (sum(query_name)/len(query_name)))