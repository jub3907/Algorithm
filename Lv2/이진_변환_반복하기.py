#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    count = 0
    del_0 = 0

    while s != "1":
        count += 1
        num = len(s)
        s = s.count("1")*"1"
        del_0 += num - len(s)
        s = len(s)
        s = bin(s)[2:]

    return [count,del_0]