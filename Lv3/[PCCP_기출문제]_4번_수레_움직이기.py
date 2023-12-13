#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/250134


# 0 : 빈칸
# 1 : 빨간 수레
# 2 : 파란 수레
# 3 : 빨간 도착
# 4 : 파란 도착

from collections import deque

def is_valid(i, j, maze, route, n, m):
    route_set = set(route)
    return 0 <= i < n and 0 <= j < m and maze[i][j] != 5  and (i, j) not in route_set

def is_valid_blue(i, j, maze, route, n, m, red_route):
    route_set = set(route)
    return 0 <= i < n and 0 <= j < m and maze[i][j] != 5  and (i, j) not in route_set and len(red_route) > len(route) and (i, j) != red_route[len(route)]


def solution(maze):
    answer = 0

    n, m = len(maze), len(maze[0])
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for i, row in enumerate(maze):
        if 1 in row:
            red_start = (i, row.index(1))
        if 2 in row:
            blue_start = (i, row.index(2))

    queue = deque([(red_start, [red_start])])
    red_routes = []

    while queue:
        position, route = queue.popleft()
        current_i, current_j = position
        for di, dj in d:
            ni, nj = current_i + di, current_j + dj
            if is_valid(ni, nj, maze, route, n, m):
                if maze[ni][nj] == 3:
                    route.append((ni, nj))
                    red_routes.append(route.copy())
                else:
                    next_route = route.copy()
                    next_route.append((ni, nj))
                    queue.append(((ni, nj), next_route))

    red_routes = sorted(red_routes, key = lambda x: len(x))
    result = []

    for red_route in red_routes:
        blue_routes = []
        blue_queue = deque([(blue_start, [blue_start])])
        
        while blue_queue:
            position, route = blue_queue.popleft()
            current_i, current_j = position
            for di, dj in d:
                ni, nj = current_i + di, current_j + dj
                if is_valid_blue(ni, nj, maze, route, n, m, red_route):
                    if maze[ni][nj] == 4:
                        route.append((ni, nj))
                        blue_routes.append(route.copy())
                    else:
                        next_route = route.copy()
                        next_route.append((ni, nj))
                        blue_queue.append(((ni, nj), next_route))

        if blue_routes:
            for blue_route in blue_routes:
                a = True

                # print(red_route, blue_route)
                for i in range(min(len(blue_route), len(red_route)) - 1):
                    if red_route[i] == blue_route[i + 1] and red_route[i + 1] == blue_route[i]:
                        a = False
                        break
                
                if a:
                    if len(red_route) > len(blue_route):
                        if blue_route[-1] not in red_route[len(blue_route):]:
                            result.append((red_route, blue_route))
                    else:
                        result.append((red_route, blue_route))
    
    if result:
        result = sorted(result, key = lambda x: max(len(x[0]), len(x[1])))

        return max(len(result[0][0]), len(result[0][1])) - 1
    else:
        return 0

solution([[1, 4], [0, 0], [2, 3]])
# solution([[1, 0, 2], [0, 0, 0], [5, 0 ,5], [4, 0, 3]])
# solution(	[[1, 5], [2, 5], [4, 5], [3, 5]])
# 
# %%
DIR = [(0, -1), (0, 1), (1, 0), (-1, 0)]

def solution(maze):
    n, m = len(maze), len(maze[0])
    red, blue, target_red, target_blue = find_positions(maze)

    global_minimum = [10**20]  # 리스트로 감싸 global 변수처럼 활용

    def brute_force(red, blue, turn, red_visited, blue_visited):
        nonlocal global_minimum

        # global_minimum을 업데이트 하는 조건!!
        if red == target_red and blue == target_blue:
            global_minimum[0] = min(global_minimum[0], turn)
            return

        red_candidates = cal_cand(red, maze, red_visited, target_red)
        blue_candidates = cal_cand(blue, maze, blue_visited, target_blue)

        for rc in red_candidates:
            for bc in blue_candidates:
                # 도달한 곳이 같으면 안된다, 자리 바꿔치기를 하면 안된다
                if rc != bc and (rc, bc) != (blue, red):
                    new_red_visited = red_visited | {rc}  # 집합 연산을 이용하여 visited 관리
                    new_blue_visited = blue_visited | {bc}

                    brute_force(rc, bc, turn + 1, new_red_visited, new_blue_visited)

    red_visited, blue_visited = {red}, {blue}

    brute_force(red, blue, 0, red_visited, blue_visited)

    return global_minimum[0] if global_minimum[0] != 10**20 else 0

def find_positions(maze):
    n, m = len(maze), len(maze[0])
    for row in range(n):
        for col in range(m):
            if maze[row][col] == 1:
                red = (row, col)
            elif maze[row][col] == 2:
                blue = (row, col)
            elif maze[row][col] == 3:
                target_red = (row, col)
            elif maze[row][col] == 4:
                target_blue = (row, col)

    return red, blue, target_red, target_blue

# cur:본인위치, maze:미로, visited: 본인 visited, target:최종 목적지
def cal_cand(cur, maze, visited, target):
    x, y = cur
    answer = []

    # 이미 도착했으면 도착한 곳을 리턴
    if cur == target:
        return [target]

    # 조건 1. 칸을 벗어나지 않는다
    # 조건 2. visited 딕셔너리에 가려는 칸이 없다
    # 조건 3. 벽이 아니다
    for dx, dy in DIR:
        if 0 <= x + dx < len(maze) and 0 <= y + dy < len(maze[0]) and (x + dx, y + dy) not in visited and \
                maze[x + dx][y + dy] != 5:
            answer.append((x + dx, y + dy))

    return answer