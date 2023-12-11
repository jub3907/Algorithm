#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/42897
# https://school.programmers.co.kr/questions/31576

# def make_set(length):
#     for i in range(length):

def solution(money):
    dp1 = [0] * len(money)
    dp1[0], dp1[1] = money[0], max(money[0], money[1])
    for i in range(2, len(money) - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])

    dp2 = [0] * len(money)
    dp2[0], dp2[1] = 0, money[1]
    for i in range(2, len(money)):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])

    return max(max(dp1), max(dp2))