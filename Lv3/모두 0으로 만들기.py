#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/76503

from collections import deque

def find_tree(a, edges):
    
    dic = {}
    
    for edge in edges:
        v1 = edge[0]
        v2 = edge[1]
        
        if v1 not in dic.keys():
            dic[v1] = []
        if v2 not in dic.keys():
            dic[v2] = []
            
        dic[v1].append(v2)
        dic[v2].append(v1)
    
    q = deque([(-1,0)])
    path = []
    visited = [0] * len(a)
    visited[0] = 1
        
    while q:
        p,c = q.popleft()
        path.append((p,c))
        
        des = dic[c]
        if des:
            for d in des:
                if not visited[d]:
                    q.append((c,d))
                    visited[d] = True
                    
    return path[::-1]

def solution(a, edges):
    answer = 0
    path = find_tree(a, edges)
    
    for parent, child in path[:-1]: 
        c_weight = a[child]
        answer += abs(c_weight)
        a[child] += -1 * c_weight
        a[parent] += c_weight
        
    if a[0] == 0:
        return answer
    
    else:
        return -1
    
    return answer