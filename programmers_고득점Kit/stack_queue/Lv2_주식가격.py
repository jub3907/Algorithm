#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        cnt = 0
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                cnt += 1
                break
            else:
                cnt += 1
        answer[i] = cnt
        
    return answer