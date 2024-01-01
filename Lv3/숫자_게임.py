from collections import deque


def solution(a, b):
    answer = 0
    a = deque(sorted(a))
    b = deque(sorted(b))
    
    while b:
        if a[0] < b[0]:
            answer += 1
            a.popleft()
            b.popleft()
        else:
            b.popleft()
            
    return answer