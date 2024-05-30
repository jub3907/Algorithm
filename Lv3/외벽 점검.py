#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/60062

from itertools import permutations

def solution(n, weak, dist):
    weak_n = len(weak)
    dist_n = len(dist)
    for i in range(weak_n): 
        weak.append(weak[i] + n)

    answer = dist_n + 1
    dist_list = list(permutations(dist, dist_n)) 

    for j in range(weak_n):
        test_weak = [weak[k] for k in range(j, j + weak_n)]
        for d in range(len(dist_list)): 
            friend_idx = 0
            cnt = 1
            friend_max_d = test_weak[0] + dist_list[d][0] 
            flag = True
            for w in range(weak_n):
                if test_weak[w] > friend_max_d: 
                    friend_idx += 1 
                    cnt += 1
                    if cnt > dist_n: 
                        flag = False
                        break
                    friend_max_d = test_weak[w] + dist_list[d][friend_idx] 
            if flag and answer > cnt:
                answer = cnt
    if answer == dist_n + 1: answer = -1
    return answer