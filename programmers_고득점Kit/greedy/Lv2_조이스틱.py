#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/42860
import string

def get_alp_to_index_dict():
    
    alp_to_index = {}
    cnt = 0
    for alp in string.ascii_uppercase:
        alp_to_index[alp] = cnt
        cnt += 1
    
    return alp_to_index

def solution(name):
    if set(name) == {"A"}:
        return 0
    
    alp_to_index = get_alp_to_index_dict()
    alp_num = len(alp_to_index.keys())
    answer = float('inf')

    
    for i in range(len(name) // 2): # 반 이상 움직일 필요 없음
        left_moved = name[-i:]+name[:-i]
        right_moved = name[i:]+name[:i]
        for n in [left_moved, right_moved[0] + right_moved[:0:-1]]:
            while n and n[-1] == 'A':
                n = n[:-1]

            row_move = i + len(n)-1
            answer = min(answer, row_move)

    for index, alp in enumerate(list(name)):
        up = alp_to_index[alp]
        down = alp_num - alp_to_index[alp]
        answer += min(up, down)

    return answer

solution("JAN")

# %%

def solution(name):
    if set(name) == {'A'}:
        return 0

    answer = float('inf')
    for i in range(len(name) // 2): # 반 이상 움직일 필요 없음
        left_moved = name[-i:]+name[:-i]
        right_moved = name[i:]+name[:i]
        for n in [left_moved, right_moved[0] + right_moved[:0:-1]]:
            while n and n[-1] == 'A':
                n = n[:-1]

            row_move = i + len(n)-1
            col_move = 0
            for c in map(ord, n):
                col_move += min(c - 65, 91 - c)

            answer = min(answer, row_move + col_move)

    return answer


solution("ABABAAAAABA")

#%%
