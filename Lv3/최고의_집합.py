#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/12938

def solution(n, s):
    answer = []

    if n > s:
        return [-1]
    
    answer = [s//n for i in range(n)]
    
    for i in range(s%n):
        answer[-i-1] += 1

    return answer