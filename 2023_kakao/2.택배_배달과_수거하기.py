#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/150369

from collections import deque

def solution(cap, n, deliveries, pickups):
    answer = 0

    pickups = deque([(index + 1, value) for index, value in enumerate(pickups)])
    deliveries = deque([(index + 1, value) for index, value in enumerate(deliveries)])

    while pickups or deliveries:
        idx_set = set()
        go, back = 0, 0
        while deliveries and go != cap:
            i, v = deliveries.pop()
            if go + v > cap:
                v -= (cap - go)
                go = cap
                deliveries.append((i, v))
            else:
                go += v

            if go != 0:
                idx_set.add(i)
            
        while pickups and back != cap:
            i, v = pickups.pop()
            if back + v > cap:
                v -= (cap - back)
                back = cap
                pickups.append((i, v))
            else:
                back += v

            if back != 0:
                idx_set.add(i)

        if idx_set:
            answer += max(idx_set) * 2

    return answer

# solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0])
# solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0])
# solution(1, 1, [], [])
solution(2, 2, [0, 0], [0, 4])