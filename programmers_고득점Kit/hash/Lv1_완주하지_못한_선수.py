#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/42576

def solution(participants, completions):
    participant_set = set(participants)
    completion_set = set(completions)
    diff_set = participant_set - completion_set
    if diff_set:
        return diff_set.pop()
    
    participant_dict = { key : 0 for key in participant_set }

    for key in participants:
        participant_dict[key] += 1
    
    for key in completions:
        participant_dict[key] -= 1

    for key, value in participant_dict.items():
        if value != 0:
            return key

solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])
