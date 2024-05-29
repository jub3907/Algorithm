#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/214288


import heapq as hq
 
def solution(k,n,reqs): 
 
    def people_info(class_num : int, people_info : list) -> dict :
        table = {i : [] for i in range(0,class_num)}
        for start,spend,class_num in people_info:
            table[class_num-1].append((start,spend))
        return table
 
    # 시간 계산 함수
    def cal_time(consultant_num : int, info : list) -> int:
        if len(info) <= consultant_num:
            return 0 
        else :
            waiting = 0
            time_list,remain_consultant = [],consultant_num
            for start,spend in info:
                if remain_consultant > 0:
                    hq.heappush(time_list,(start+spend)) 
                    remain_consultant += -1
                else:
                    now_time = hq.heappop(time_list) 
                    if now_time - start > 0:
                        waiting += now_time - start 
                        hq.heappush(time_list,(now_time+spend))
                    else :
                        hq.heappush(time_list,(start+spend))
            return waiting
 
    infos = people_info(k,reqs)
    time_info = [[0]*(n-k+2) for _ in range(k)] 
    for class_n in range(k):
        for conslut_n in range(1,n-k+2): 
            time = cal_time(conslut_n,infos[class_n])
            time_info[class_n][conslut_n] = time
            if not time:
                break
 
    count = [1]*k
    while sum(count)<n:
        temp = []
        for i in range(k):
            temp.append(time_info[i][count[i]+1]-time_info[i][count[i]])
        min_idx = temp.index(min(temp))
        count[min_idx] += 1
 
    min_time = 0
    for class_n,conslut_n in enumerate(count):
        min_time += time_info[class_n][conslut_n]
    return min_time