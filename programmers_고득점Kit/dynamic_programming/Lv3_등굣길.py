#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/42898
def solution(m, n, puddles):
    if m == 1 or n == 1:
        return 1
    
    matrix = [[0 for j in range(m)] for i in range(n)]
    puddles = {(j-1, i-1) for i, j in puddles}

    matrix[0][0] = 1


    for i, floor in enumerate(matrix):
        for j, value in enumerate(floor):
            if (i, j) in puddles:
                continue
            if i == 0 and j == 0:
                continue
            elif i == 0:
                matrix[i][j] += matrix[i][j - 1]
            elif j == 0:
                matrix[i][j] += matrix[i - 1][j]
            else:
                matrix[i][j] += (matrix[i - 1][j] + matrix[i][j - 1])

    return matrix[-1][-1] % 1000000007

solution(4, 3, [[2, 2]])
# %%
