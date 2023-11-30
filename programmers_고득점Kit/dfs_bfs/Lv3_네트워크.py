#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/43162

from collections import deque

def solution(n, computers):
    answer = 0
    node_set = {i for i in range(n)}
    visited_set = set()
    remain_nodes = {i for i in range(n)}

    visited = set()
    queue = deque([0])
    while visited_set != node_set:
        if queue:
            node = queue.popleft()
            if node in visited:
                continue
            else:
                visited.add(node)
                edges = [i for i, x in enumerate(computers[node]) if x == 1 and i not in visited]
                for node in edges:
                    queue.append(node)
        else:
            answer += 1
            visited_set = visited_set | visited
            remain_nodes = list(remain_nodes - visited)
            if not remain_nodes:
                break
            visited = set()
            queue.append(remain_nodes[0])
            remain_nodes = set(remain_nodes)

    return answer

solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
# %%
a = deque()
a.append(1)
a.append(2)
a.append(3)
a.popleft()
# %%

[1, 1, 1, 0, 0, 1, 1, 1].index(1)
# %%
a  = {1, 2}
b = {2, 3, 4}
a | b
# %%
# %%

