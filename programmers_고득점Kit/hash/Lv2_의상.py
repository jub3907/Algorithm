#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    dic = {}

    for item, key in clothes:
        if key in dic.keys():
            dic[key].append(item)
        else:
            dic[key] = [item]

    answer = 1
    for key, value in dic.items():
        answer *= (len(value) + 1)
    
    return answer - 1

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])
# %%
