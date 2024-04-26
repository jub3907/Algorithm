#%%
# https://velog.io/@mrbartrns/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%B9%B4%EC%9A%B4%ED%8A%B8-%EB%8B%A4%EC%9A%B4-python-wrf2b02u

INF = 987654321

def create_table():
    arr = []
    arr.append([i for i in range(1, 21)])
    arr[0].append(50)
    nxt = []
    for i in range(1, 21):
        for j in range(2, 4):
            ret = i * j
            
            if ret > 20:
                nxt.append(ret)
                
    arr.append(list(set(nxt)))
    
    return arr

def solution(target):
    table = create_table()

    dp = [[INF, 0] for _ in range(target + 1)]
    dp[0][0] = 0

    for i in range(1, target + 1):
        for j in range(2):
            for k in range(len(table[j])):
                prev = i - table[j][k]

                if prev < 0:
                    continue

                total, valid = dp[prev][0] + 1, dp[prev][1] + 1 - j

                if total < dp[i][0]:
                    dp[i] = [total, valid]
                    
                elif total == dp[i][0]:
                    dp[i] = [total, max(dp[i][1], valid)]

    return dp[target]