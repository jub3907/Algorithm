#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/42747
def solution(citations):
    citations = sorted(citations, reverse= True)
    h = 0

    for i in range(0, len(citations)):
        if citations[i] >= i + 1:
            h = i + 1
        else:
            break
    return h

solution( [6, 5, 3, 3, 0])