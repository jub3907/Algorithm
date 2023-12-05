#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/84021
from collections import deque

def add_block_rotation(blocks):
    def rotated(array_2d):
        list_of_tuples = zip(*array_2d[::-1])
        return [list(e) for e in list_of_tuples]

    for key, value in blocks.items():
        ro_90 = rotated(value[0])
        ro_180 = rotated(ro_90)
        ro_270 = rotated(ro_180)
        blocks[key] += [ro_90, ro_180, ro_270]

def search_table(table, i, j, blocks):
    table[i][j] = 2
    queue, visited = deque([(i, j)]), {(i, j)}

    valid_block_count = 1

    d = {(-1, 0), (1, 0), (0, -1), (0, 1)}

    min_x, min_y, max_x, max_y = i, j, i, j

    while queue:
        i, j = queue.popleft()
        for dx, dy in d:
            nx, ny = i + dx, j + dy
            if 0 <= nx < len(table) and 0 <= ny < len(table) and (nx, ny) not in visited and table[nx][ny] == 1:
                queue.append((nx, ny))
                visited.add((nx, ny))
                table[nx][ny] = 2
                valid_block_count += 1

                min_x = nx if nx < min_x else min_x
                max_x = nx if max_x < nx else max_x
                min_y = ny if ny < min_y else min_y
                max_y = ny if max_y < ny else max_y


    block_shape = [[table[i][j] for j in range(min_y, max_y + 1)] for i in range(min_x, max_x + 1)]

    need_block_count = (max_x - min_x + 1) * (max_y - min_y + 1)
    # key : (인덱스, 0을 포함한 필요한 블록 개수, 0을 제외한 필요한 블록 개수)
    key = (len(blocks.keys()), need_block_count, valid_block_count)
    blocks[key] = [block_shape]

    
def search_board(board, i, j, blocks):
    board[i][j] = 2
    queue, visited = deque([(i, j)]), {(i, j)}
    valid_block_count = 1

    d = {(-1, 0), (1, 0), (0, -1), (0, 1)}

    min_x, min_y, max_x, max_y = i, j, i, j

    while queue:
        i, j = queue.popleft()
        for dx, dy in d:
            nx, ny = i + dx, j + dy
            if 0 <= nx < len(board) and 0 <= ny < len(board) and (nx, ny) not in visited and board[nx][ny] == 1:
                queue.append((nx, ny))
                visited.add((nx, ny))
                board[nx][ny] = 2
                valid_block_count += 1
                
                min_x = nx if nx < min_x else min_x
                max_x = nx if max_x < nx else max_x
                min_y = ny if ny < min_y else min_y
                max_y = ny if max_y < ny else max_y


    need_block_count = (max_x - min_x + 1) * (max_y - min_y + 1)
    condition = lambda x: (x[1] == need_block_count and x[2] == valid_block_count)
    keys = list(filter(condition, blocks.keys()))
    
    if keys:
        block_shape = [[board[i][j] for j in range(min_y, max_y + 1)] for i in range(min_x, max_x + 1)]

        for key in keys:
            matrixes = blocks[key]
            for matrix in matrixes:
                if block_shape == matrix:
                    del(blocks[key])
                    return key[2]

    return 0

def solution(game_board, table):
    answer = 0
    blocks = dict()
    # board의 0 -> 1, 1 -> 0 변환
    game_board = [[0 if item == 1 else 1 for item in row] for row in game_board]

    for i in range(len(table)):
        for j in range(len(table)):
            if table[i][j] == 1:
                search_table(table, i, j, blocks)
        
    add_block_rotation(blocks)
    
    for i in range(len(game_board)):
        for j in range(len(game_board)):
            if game_board[i][j] == 1:
                answer += search_board(game_board, i, j, blocks)

    return answer

solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]], [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]])
# solution([[0,0,0],[1,1,0],[1,1,1]], 	[[1,1,1],[1,0,0],[0,0,0]])
# %%
a = [[2, 2, 2], [2, 0, 0]]
b = [[2, 2, 2], [2, 0, 0]]

a == b
# %%
