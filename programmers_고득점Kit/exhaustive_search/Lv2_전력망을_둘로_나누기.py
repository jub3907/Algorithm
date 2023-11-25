#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/86971
# 테스트케이스 8번 실패

from collections import deque

def search_node(n, wires, edges):
    visited = set()
    queue = deque()
    i, j = wires[0]
    
    queue.append(i)
    queue.append(j)

    while queue:
        node = queue.pop()
        if node in visited:
            continue

        connected_nodes = edges[node]
        del(edges[node])
        for c_node in connected_nodes:
            queue.append(c_node)

        visited.add(node)
    
    a, b = len(visited), len(edges.keys())
    return max(a, b) - min(a, b)

def solution(n, wires):
    answer = n

    edges = {i: [] for i in range(1, n + 1)}
    for i, j in wires:
        edges[i].append(j)
        edges[j].append(i)

    for i in range(len(wires)):
        i, j = wires[i]
        tmp_wires = wires[:i] + wires[i + 1:]
        tmp_edges = edges.copy()
        tmp_edges[i].remove(j)
        tmp_edges[j].remove(i)

        diff = search_node(n, tmp_wires, tmp_edges)
        if answer > diff:
            answer = diff

    return answer

solution(8,[[1,2],[1,3],[1,4],[4,5],[5,6],[6,7],[6,8]])

# %%

# 정답 : https://school.programmers.co.kr/questions/50818
def solution(n, wires):
    answer = -1
    saveWires = wires.copy()
    countList = []
    count = 0

    for comb in wires.copy():
        saveWires.remove(comb)
        setl = set([comb[0]])
        print(setl)
        previous = set()
        while (setl != previous) :
            previous = setl.copy()
            for wire in saveWires.copy():
                if (setl & set(wire)):
                    setl = setl | set(wire)
        countList.append(abs((n - 2*len(setl))))
        count = 0
        saveWires = wires.copy()

    answer = min(countList)
    return answer

solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])