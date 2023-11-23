#%% 
# https://school.programmers.co.kr/learn/courses/30/lessons/42626
from heapq import *

def solution(scoville, K):
    answer = 0
    heapify(scoville)

    while scoville[0] < K and len(scoville) > 1:
        first = heappop(scoville)
        second = heappop(scoville)
        heappush(scoville, first + second * 2)
        answer += 1
        
    
    return answer if scoville[0] >= K else -1

solution( [0, 0, 5, 5, 5],2)
# %%
