#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/12945
def solution(n):
    fib=[0,1]
    for i in range(2, n+1):
        fib.append((fib[i-2]+fib[i-1])%1234567)
    return fib[-1]