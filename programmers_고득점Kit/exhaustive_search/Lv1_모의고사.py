#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    result = []

    a_answer = [1, 2, 3, 4, 5] * 2000
    b_answer = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    c_answer = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    

    a_score, b_score, c_score = 0, 0, 0
    for answer, a, b, c in zip(answers, a_answer, b_answer, c_answer):
        if answer == a:
            a_score += 1
        if answer == b:
            b_score += 1
        if answer == c:
            c_score += 1
    
    max_score = max([a_score, b_score, c_score])
    if a_score == max_score:
        result.append(1)
    if b_score == max_score:
        result.append(2)
    if c_score == max_score:
        result.append(3)

    return sorted(result)
