
#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/42884

import heapq

def solution(routes):
    routes = [[j, i] for i, j in routes]
    heapq.heapify(routes)
    cameras = []

    while routes:
        j, i = heapq.heappop(routes)
        camera = j
        cameras.append(j)
        while routes:
            j, i = heapq.heappop(routes)
            if i <= camera <= j:
                continue
            else:
                heapq.heappush(routes, [j, i])
                break
        

    return len(cameras)

solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])
# %%
