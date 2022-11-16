"""
Question : https://www.hackerrank.com/challenges/merge-the-tools/problem
Difficulty : Medium
Max Score : 40

"""

def merge_the_tools(string, k):
    s = string
    k = k

    if len(s)/k:
        d = (round(len(s)/k))
    if k == 1:
        for i in s:
            print(i)
    else:
        s_split =  []
        for i in range(d):
            new = s[:k]
            s_split.append(new)
            s = s.replace(s[:k], '')

        for word in s_split:
            output = []
            for c in word:
                if c not in output:
                    output.append(c)
            output = ''.join(output)
            print(output)

