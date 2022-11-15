"""
Question : https://www.hackerrank.com/challenges/the-minion-game/problem
Difficulty : Medium
Max Score : 40

"""

def minion_game(string):
    strlen = len(string)
    vcnt, ccnt = 0,0

    for i in range(strlen):
        if string[i] in 'AEIOU':
            vcnt = vcnt + (strlen - i)
        else:
            ccnt = ccnt + (strlen - i)
            
    if ccnt > vcnt:
        print("Stuart {0}".format(ccnt))
    elif ccnt < vcnt:                        
        print("Kevin {0}".format(vcnt))
    else:
        print("Draw")    
