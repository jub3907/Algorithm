#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/131705
def solution (number) :
    from itertools import combinations
    cnt = 0
    for i in combinations(number,3) :
        if sum(i) == 0 :
            cnt += 1
    return cnt