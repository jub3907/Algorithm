#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    words = s.split(" ")
    result = []
    
    for char in words:
        if char != "":
            result.append(char[0].upper() + char[1:].lower())
        else:
            result.append("")
    
    return " ".join(result)