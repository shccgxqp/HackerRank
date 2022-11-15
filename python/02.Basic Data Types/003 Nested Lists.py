"""
Question : https://www.hackerrank.com/challenges/nested-list/problem
Difficul : tyEasy
Max Score : 5

"""

if __name__ == '__main__':
    
    student = {}
    a = 0
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student[name] = score
    else:
        a = list(set(student.values()))
        a.sort()
        names = sorted(student.keys())
        for name in names:
            if student[name] == a[1] :
                print(name)

