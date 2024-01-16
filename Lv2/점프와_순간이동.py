#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/12980
def solution(N):
    answer = 0
    while N > 0:
        answer += N % 2
        N //= 2
    return answer