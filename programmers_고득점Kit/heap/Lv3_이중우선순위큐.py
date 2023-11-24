#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/42628

from heapq import *

def solution(operations):
    max_heap = []
    min_heap = []

    for operation in operations:
        oper, value = operation.split()
        value = int(value)

        if oper == "I":
            heappush(max_heap, -value)
            heappush(min_heap, value)
        else:
            if max_heap:
                if value == 1:
                    max_value = -heappop(max_heap)
                    min_heap.remove(max_value)
                    heapify(min_heap)
                else:
                    min_value = heappop(min_heap)
                    max_heap.remove(-min_value)
                    heapify(max_heap)

    if len(max_heap) >= 2:
        max = -heappop(max_heap)
        min_heap.remove(max)
        heapify(min_heap)
        min = heappop(min_heap)

        return [max, min]
    
    elif len(max_heap) == 1:
        max = -heappop(max_heap)

        return [max, max]
    
    else:
        return [0, 0]

solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])
# %%
