#%%
from collections import deque

def solution(start_x, start_y, path):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    queue = deque([start_x, start_y])
    visited = set([(start_x, start_y)])

    while queue:
        x, y = queue.popleft()
        for i, j in zip(dx, dy):
            nx, ny = x + i, y + j
            if True: #범위에 맞으면
                if (nx, ny) not in visited:
                    queue.append((nx, ny))
                    visited.append((nx, ny))

    