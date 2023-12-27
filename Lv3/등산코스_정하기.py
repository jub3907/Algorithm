#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/118669
from collections import defaultdict
import heapq

INF = int(1e9)

def solution(n, paths, gates, summits):
    summits = sorted(summits)
    graph = defaultdict(list)
    for p in paths:
        a, b, c = p
        # 양방향인데, 출발, 목적과 연결된 통로는 단방향 설정하면 조건 확인이 편하다.
        if a in gates or b in summits:
            graph[a].append((b, c))
        elif a in summits or b in gates:
            graph[b].append((a, c))
        else:
            graph[a].append((b, c))
            graph[b].append((a, c))

    def dijkstra():
        q = []
        intensity = [INF] * (n+1)
        for g in gates:
            intensity[g] = 0
            heapq.heappush(q, (0, g))
        while q:
            n_weight, now = heapq.heappop(q)
            if intensity[now] < n_weight:
                continue
            for e in graph[now]:
                to = e[0]
                w = e[1]
                if intensity[to] > max(intensity[now], w):
                    intensity[to] = max(intensity[now], w)
                    heapq.heappush(q, (intensity[to], to))
        return intensity
    
    intensity = dijkstra()
    summits = sorted(summits, key=lambda x: (intensity[x], x))
    return [summits[0], intensity[summits[0]]]

#%%
from collections import defaultdict
import heapq
def solution(n, paths, gates, summits):
    answer = []
    graph = defaultdict(list)
    s = []
    INF = float('inf')
    node_intensity_info = [INF]*(n+1)
    # set 을사용하지않으면 list 내의 in 확인은 O(N) 이라 시간초과뜬다
    summits= set(summits)
    # 출발지점 의 (intensitiy는 0 으로 , gate 번호) 
    for g in gates:
        heapq.heappush(s,(0,g))
        node_intensity_info[g] = 0
    # 출발지점 -> 도착지점 -> 출발지점
    for i,j,w in paths:
        graph[i].append((j,w))
        graph[j].append((i,w))
    # 출발지점 돌면서
    while s:
        inten,node = heapq.heappop(s)
        if node in summits or inten > node_intensity_info[node]:
            continue
        # node 의 inten 저장해주고
        for next_node,next_intensity in graph[node]:
            # 현재 intensity 와 다음 노드로가는 next_intensity 와 node_intensity_info 를 비교해야함
            # 즉 intensity 에는 현재와 다음 노드 intensity 를 비교해주고
            intensity = max(inten,next_intensity)
            # 그게 기록일지 (next_node_info) 보다 작다면 갱신해주고 heap 에넣어줌
            if intensity < node_intensity_info[next_node]:
                node_intensity_info[next_node] = intensity
                heapq.heappush(s,(node_intensity_info[next_node],next_node))
    answer = []
    for summit in summits:
        answer.append([summit,node_intensity_info[summit]])
    answer.sort(key = lambda x: (x[1],x[0]))
    return answer[0]