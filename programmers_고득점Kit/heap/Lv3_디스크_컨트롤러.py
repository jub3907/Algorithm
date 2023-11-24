#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/42627

from heapq import *

def solution(jobs):
    work_count = len(jobs)
    current_jobs = []
    heapify(jobs)
    time = 0
    answer = 0


    while jobs or current_jobs:
        if jobs and jobs[0][0] <= time:
            start, work = heappop(jobs)
            heappush(current_jobs, (work, start))
        elif current_jobs:
            work, start = heappop(current_jobs)
            answer += work + time - start
            time += work
        else:
            start, work = heappop(jobs)
            answer += work
            time = start + work

    return answer // work_count

solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]])
# %%
