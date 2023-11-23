#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    queue = priorities
    dic = { i : 0 for i in set(priorities) }
    max_priority_set = set(priorities)
    max_priority = max(max_priority_set)


    for priority in priorities:
        dic[priority] += 1
    
    pop_count = 0

    while True:
        priority = queue.pop(0)
        if priority == max_priority:
            dic[priority] -= 1
            pop_count += 1
            if location == 0:
                return pop_count
            
            if dic[priority] == 0:
                max_priority_set.remove(max_priority)
                max_priority = max(max_priority_set)
            
        else:
            queue.append(priority)

        location -= 1
        if location < 0:
            location = len(queue) - 1

solution([1, 1, 9, 1, 1, 1], 0)