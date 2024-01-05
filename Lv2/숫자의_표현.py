#%% 
# https://school.programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    ans = 0
    left, right, cnt = 0,0,0

    while left < n:
        if cnt < n:
            right += 1
            cnt += right
        else:
            if n == cnt: ans += 1
            left += 1
            cnt -= left

    return ans