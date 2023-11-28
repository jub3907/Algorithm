#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/42861

# 시간 초과
from collections import deque

def solution(n, costs):
    answer = float('inf')
    min_cost = float('inf')
    node_set = {i for i in range(n)}
    graph = [[0 for j in range(n)] for i in range(n)]

    for i, j, cost in costs:
        graph[i][j] = cost
        graph[j][i] = cost

    for start in range(n):
        tmp_answer = 0
        visited = set()

        current = start
        next_node = current
        visited.add(current)

        queue = deque()
        while node_set != visited:
            tmp_min = float('inf')
            for node in node_set - visited:
                if graph[current][node] == 0:
                    continue
                if tmp_min >= graph[current][node]:
                    tmp_min = graph[current][node]
                    next_node = node
            
            tmp_answer += tmp_min
            current = next_node
            visited.add(current)
            # print('visited', visited)

        if tmp_answer < answer:
            answer = tmp_answer

    return answer

solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])
# %%
# 성공

import heapq

def solution(n, costs):
    answer = float('inf')
    node_set = {i for i in range(n)}
    graph = [[0 for j in range(n)] for i in range(n)]
    

    for i, j, cost in costs:
        graph[i][j] = cost
        graph[j][i] = cost

    current = 0
    answer = 0
    visited = set([current])
    next_edges = [(cost, j) for j, cost in enumerate(graph[current])]
    heapq.heapify(next_edges)
    while visited != node_set:
        cost, j = heapq.heappop(next_edges)
        if j in visited or cost == 0:
            continue
        else:
            answer += cost
            visited.add(j)
            current = j
            for node, cost in enumerate(graph[current]):
                if node not in visited and cost != 0:
                    heapq.heappush(next_edges, (cost, node))

    return answer
        
solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])
