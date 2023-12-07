#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/49191

from collections import deque

def solution(n, results):
    defeat = {i : set() for i in range(n)}
    win = {i : set() for i in range(n)}
    for i, j in results:
        i -= 1
        j -= 1

        defeat[j].add(i)
        win[i].add(j)

    answer = 0

    for node in range(n):
        queue = deque([node])
        visited = set()
        cnt = 0

        while queue:
            current = queue.popleft()
            for next_node in defeat[current]:
                if next_node not in visited:
                    cnt += 1
                    visited.add(next_node)
                    queue.append(next_node)

        queue = deque([node])
        while queue:
            current = queue.popleft()
            for next_node in win[current]:
                if next_node not in visited:
                    cnt += 1
                    visited.add(next_node)
                    queue.append(next_node)
        if cnt == n - 1:
            answer += 1
        
    return answer


solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])
# %%
