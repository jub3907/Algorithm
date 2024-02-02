#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/64063

def solution(k, room_number): # 정확성100 효율성0
    answer = [-1]
    room_chk = [0]*(k+1) # 0:빈방 1:이미 배정된 방
    for num in room_number:
        if num not in answer: # 해당 방이 빈 방이면
            answer.append(num) # 바로 배정
            room_chk[num] = 1
        else:
            for idx in range(num+1, k+1): # 빈방 찾기
                if room_chk[idx] == 0:
                    answer.append(idx)
                    room_chk[idx] =1
                    break
    answer = answer[1:]
    return answer

#%%

import sys
sys.setrecursionlimit(10000)

def solution(k, room_number):
    rooms = dict()
    for num in room_number:
        find_emptyroom(num,rooms)
    return list(rooms.keys())

def find_emptyroom(num, rooms): 
    if num not in rooms.keys(): 
        rooms[num] = num + 1
        return num 
    empty = find_emptyroom(rooms[num], rooms) 
    rooms[num] = empty + 1 
    return empty 