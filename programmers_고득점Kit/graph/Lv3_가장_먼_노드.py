#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/49189



def solution(n, edge):
    edges = {i : set() for i in range(n)}
    for i, j in edge:
        i -= 1
        j -= 1
        edges[i].add(j)
        edges[j].add(i)

    dist = dict()
    dist[1] = edges[0]
    used_node = set(edges[0])
    used_node.add(0)
    
    distance = 2
    while dist[distance - 1]:
        dist[distance] = []
        current_nodes = dist[distance-1]
        for current_node in current_nodes:
            for next_node in edges[current_node]:
                if next_node in used_node:
                    continue
                else:
                    dist[distance].append(next_node)
                    used_node.add(next_node)
            
        distance += 1

    return len(dist[distance - 2])

solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
# %%
