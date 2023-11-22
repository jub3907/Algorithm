#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    answer = []
    while progresses:
        count = 0
        while progresses and progresses[0] >= 100:
            del(progresses[0])
            del(speeds[0])
            count += 1


        progresses = [a + b for a, b in zip(progresses, speeds)]

        if (count != 0 ):
            answer.append(count)
    return answer

solution([93, 30, 55], [1, 30, 5])