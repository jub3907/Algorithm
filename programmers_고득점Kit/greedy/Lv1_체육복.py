#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    lost_set = set(lost)
    reserve_set = set(reserve)

    both = lost_set & reserve_set
    lost = lost_set - both
    reserve = sorted(list(reserve_set - both))

    have = [True] * n
    for i in lost:
        have[i - 1] = False

    while reserve:
        i = reserve.pop(0) - 1
        if have[i] == False:
            have[i] = True
        elif i != 0 and have[i - 1] == False:
            have[i - 1] = True
        elif i != n - 1 and have[i + 1] == False:
            have[i + 1] = True
    
    return have.count(True)

solution(5, [4, 5], [3, 4])
# %%
