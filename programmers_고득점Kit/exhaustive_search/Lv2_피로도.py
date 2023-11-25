#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/87946

import itertools

def solution(k, dungeons):
    pers = list(itertools.permutations(dungeons))
    answer = 0
    for per in pers:
        tmp_k = k
        tmp_answer = 0
        for need, consume in per:
            if tmp_k >= need:
                tmp_k -= consume
                tmp_answer += 1
        
        if tmp_answer > answer:
            answer = tmp_answer

    return answer

solution(80, [[80,20],[50,40],[30,10]])
# %%
