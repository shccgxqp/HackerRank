"""
Question : https://www.hackerrank.com/challenges/python-lists/problem
Difficul : tyEasy
Max Score : 5

"""

if __name__ == '__main__':
    N = int(input())
    list1 = []
    count = 0

    while count < N:
        user_input = input().strip().replace(" ", "")

        if user_input == "print":
            print(list1)
        elif user_input == "sort":
            list1.sort()
        elif user_input == "pop":
            list1.pop()
        elif user_input == "reverse":
            list1.reverse()
        elif user_input[:6] == 'remove':
            user_input = user_input[6:]
            list1.remove(int(user_input[-1]))
        elif user_input[:6] == 'append':
            list1.append(int(user_input[6:]))
        elif user_input[:6] == 'insert':
            user_input = user_input[6:]
            list1.insert(int(user_input[0]), int(user_input[1:]))
        count += 1
