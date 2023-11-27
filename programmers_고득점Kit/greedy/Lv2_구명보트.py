#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/42885

def get_remain_people_count(weight_dict):
    return sum(weight_dict.values())

def solution(people, limit):
    weight_set = set(people)
    
    under_half = set(filter(lambda x: x <= (limit // 2), weight_set))
    if not under_half:
        return len(people)
    
    weight_dict = {i: 0 for i in weight_set}
    remain = 0
    for weight in people:
        weight_dict[weight] += 1

    answer = 0
    remain = sum(weight_dict.values())


    while remain != 0:
        target = limit
        cnt = 0

        max_weight = max(weight_set)
        if weight_dict[max_weight] == 1:
            weight_dict[max_weight] -= 1
            cnt += 1
            target -= max_weight
        elif max_weight <= target / 2:
            weight_dict[max_weight] -= 2
            cnt += 2

        if weight_dict[max_weight] == 0:
            weight_set.remove(max_weight)


        if weight_set and cnt != 2:
            min_weight = min(weight_set)
            if target >= min_weight:
                cnt += 1
                weight_dict[min_weight] -= 1
                if weight_dict[min_weight] == 0:
                    weight_set.remove(min_weight)
            

        answer += 1
        remain -= cnt

    print("answer", answer)
    return answer

solution([70, 50, 80, 50], 100)
solution([70, 80, 50], 100)
solution([30, 40, 50, 60], 100)
solution([40, 40, 40], 120)
solution( [10, 50, 100], 160)
# %%


def get_remain_people_count(weight_dict):
    return sum(weight_dict.values())

def solution(people, limit):
    weight_set = set(people)
    
    under_half = set(filter(lambda x: x <= (limit // 2), weight_set))
    if not under_half:
        return len(people)
    
    over_half = set(filter(lambda x: x >= (limit // 2), weight_set))
    if not over_half:
        return len(people) / 2 if len(people) % 2 == 0 else (len(people) // 2) + 1
    
    weight_dict = {i: 0 for i in weight_set}
    for weight in people:
        weight_dict[weight] += 1

    answer = 0
    remain = sum(weight_dict.values())
    target = limit


    while remain != 0:
        cnt = 0
        max_weight = max(weight_set) if weight_set else 240
        while weight_set and cnt != 2 and target >= max_weight:
            target -= max_weight
            cnt += 1
            weight_dict[max_weight] -= 1
            if weight_dict[max_weight] == 0:
                weight_set.remove(max_weight)
                break
        
        min_weight = min(weight_set) if weight_set else 0
        while weight_set and cnt != 2 and target >= min_weight:
            cnt += 1
            target -= min_weight
            weight_dict[min_weight] -= 1
            if weight_dict[min_weight] == 0:
                weight_set.remove(min_weight)
                min_weight = min(weight_set) if weight_set else 0

        answer += 1
        remain -= cnt
        target = limit

    # print("answer", answer)
    return answer

#%%
from collections import deque

def solution(people, limit):
    answer = 0 
    deq = deque(sorted(people))
    
    while len(deq) > 1:
        if deq[0] + deq[-1] > limit:
            deq.pop()
            answer += 1
        else:
            deq.pop()
            deq.popleft()
            answer += 1
    if deq:
        answer += 1
    
    return answer
