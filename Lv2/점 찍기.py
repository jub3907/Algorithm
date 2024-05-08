#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/140107
import math

def solution(k, d):
    answer = 0
    for x in range(0, d + 1, k):
        res_d = math.floor(math.sqrt(d*d - x*x))
        answer += (res_d // k) + 1
    return answer 