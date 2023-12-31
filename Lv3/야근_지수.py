#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/12927

from heapq import heapify, heappush, heappop


def solution(n, works):
    if sum(works) <= n:
        return 0

    works = [(-1) * work for work in works]
    heapify(works)
    while n:
        curr_work = heappop(works)
        post_work = curr_work + 1
        heappush(works, post_work)
        n -= 1

    return sum([work ** 2 for work in works])