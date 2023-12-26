#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/132266

from collections import deque

def solution(n, roads, sources, destination):
    edges = {i: [] for i in range(n)}
    for i, j in roads:
        i -= 1
        j -= 1
        edges[i].append(j)
        edges[j].append(i)

    min_dest_set = set()
    destination -= 1
    answer = []
    
    for source in sources:
        source -= 1
        if source == destination:
            answer.append(0)
            continue
        visited = set([source])
        queue = deque()
        queue.append((source, visited.copy()))
        while queue:
            current, visited = queue.popleft()
            if current == destination:
                break
            next_nodes = edges[current]
            for node in next_nodes:
                if node not in visited:
                    new_visited = visited.copy()
                    new_visited.add(node)
                    queue.append([node, new_visited])
        
        if current == destination:
            min_dest[(source, )]
            answer.append(len(visited) - 1)
        else:
            answer.append(-1)

    return answer

solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5)
# solution(3, [[1, 2], [2, 3]], [2, 3], 1)

# %%

from collections import deque
def solution(n, roads, sources, destination):
    answer = []
    graph = dict()
    # 그래프 초기화
    for i in range(1,n+1):
        graph[i] = []

    for a,b in roads:
        graph[a].append(b)
        graph[b].append(a)

    # destination 에서 각 source 까지의 거리
    distance = [-1] * (n+1)

    # bfs 로 탐색
    q = deque()
    # 목적지에서 탐색 시작, 목적지와 초기 거리(0) 을 넣는다.
    q.append([destination,0])
    # 이미 방문한적 있는지 검사
    visited = set()

    while q:
        v,l = q.popleft()
        # 방문한 적 있으면 넘어간다.
        if v in visited:
            continue
        # 방문한 적 없으면 방문 기록에 남기고
        visited.add(v)
        # destination 으로 부터의 거리를 저장한다.
        distance[v] = l

        # 현재 노드에서 갈 수 있는 다른 노드를 큐에 넣는다.
        # 각 간선의 거리는 1이므로, 다음 노드까지의 거리는 현재 거리 + 1
        for next in graph[v]:
            q.append([next,l+1])
    # 각 source 들과 destination 과의 거리를 정답에 넣는다.
    # distance 는 -1로 초기화해서, 도착하지 못하는 경우는 -1 이 들어간다.
    for s in sources:
        answer.append(distance[s])
    return answer