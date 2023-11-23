#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/42583

def solution(bridge_length, weight, truck_weights):
    after = []
    acrossing = []
    acrossing_time = []
    time = 0
    waiting = truck_weights

    while acrossing != [] or waiting != []:
        time += 1
        if waiting:
            truck = waiting.pop(0)
            if bridge_length != len(acrossing_time) and sum(acrossing) + truck <= weight:
                acrossing.append(truck)
                acrossing_time.append(0)
            else:
                waiting = [truck] + waiting

        tmp = []
        for i in acrossing_time:
            if i + 2 > bridge_length:
                after.append(acrossing.pop(0))
            else:
                tmp.append(i + 1)
                        
        acrossing_time = tmp

    return time + 1

solution(2, 10, [7,4,5,6])
# %%
