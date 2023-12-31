#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/12973
def solution(s):
    
    stack = [] 
    
    for i in s:
        if stack and stack[-1] == i:
            stack.pop()
            continue  
        
        stack.append(i)
    return int(not stack)