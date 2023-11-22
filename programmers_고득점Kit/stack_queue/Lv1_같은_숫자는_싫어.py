#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = []
    prev = None

    for item in arr:
        if item == prev:
            continue
        else:
            answer.append(item)
            prev = item

    return answer