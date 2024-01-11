#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/1843

def solution(arr):
    arr = ''.join(arr).split('-') 
    a0 = sum([*map(int, arr[0].split('+'))]) 

    min_tail, max_tail = 0, 0    
    
    for a in arr[:0:-1]: 
        sub = [*map(int, a.split('+'))]
        min_sub = -sum(sub)             
        max_sub = -2*sub[0] -min_sub    
        max_tail = max(max_sub +max_tail, min_sub -min_tail)
        min_tail = min(min_sub +min_tail, min_sub -max_tail)
        
    return a0 + max_tail