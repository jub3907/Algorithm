#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/87390

def solution(n, left, right):
    result = []
    for i in range(left, right+1):
        
        y, x = i//n, i%n
        value = max(y,x) + 1
        
        result.append(value)
    
    return result