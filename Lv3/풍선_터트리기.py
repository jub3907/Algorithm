#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/68646

def solution(a):
    answer = 0
    min_dp = [float('inf')] * len(a)
    min_dp[0] = a[0]
    
    for i in range(1, len(a)):
        min_dp[i] = min(min_dp[i-1], a[i])

    min_dp[-1] = a[-1]
    for i in range(len(a)-2,0, -1):
        if a[i] < min_dp[i-1] and a[i] < min_dp[i+1]:
            answer += 1
        elif (min_dp[i - 1] < a[i] < min_dp[i + 1]) or (min_dp[i - 1] > a[i] > min_dp[i + 1]):
            answer += 1
        else:
            pass
        min_dp[i] = min(min_dp[i+1], a[i])
    return answer + 2