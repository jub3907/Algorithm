#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    answer = 0
    double = bin(n)[2:]
    for number in range(n+1, 1000000):
        next_double = bin(number)[2:]
        if next_double.count("1") == double.count("1"):
            answer = number
            break
        else:
            pass
    return answer