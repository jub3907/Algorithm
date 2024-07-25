#%%
# https://www.acmicpc.net/problem/1012

def dfs(y, x):
    graph[y][x] = 0
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dy, dx in d:
        Y, X = y+dy, x+dx
        if (0 <= Y < N) and (0 <= X < M) and graph[Y][X] == 1:
            dfs(Y, X)

for case in range(int(input())):
    M, N, K = map(int, input().split())
    graph = [[0]*M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1
    res = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                dfs(i, j)
                res += 1
    print(res)