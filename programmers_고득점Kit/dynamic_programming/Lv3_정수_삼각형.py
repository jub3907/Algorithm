#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    triangle = [i + [-1] * (len(triangle) - len(i)) for i in triangle]
    for i, floor in enumerate(triangle):
        if i == 0:
            continue
        for j, value in enumerate(floor):
            if j == 0:
                triangle[i][j] += triangle[i - 1][j]
            else:
                triangle[i][j] += max(triangle[i - 1][j], triangle[i - 1][j - 1])
    
    return max(triangle[-1])

solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
# %%
