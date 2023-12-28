#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/138475

import math


def get_prime_set(n):
    array = [True for i in range(n + 1)] 

    for i in range(2, int(math.sqrt(n)) + 1): 
        if array[i] == True: 
            j = 2 
            while i * j <= n:
                array[i * j] = False
                j += 1

    prime_set = set()

    for i in range(2, n + 1):
        if array[i]:
            prime_set.add(i)
    
    return prime_set

def solution(e, starts):
    answer = []
    prime_set = get_prime_set(e)
    prime_list = sorted(list(prime_set))

    start_set = set(starts)
    start = min(start_set)
    end = e
    results = []

    for num in range(start, end + 1):
        if num in prime_set:
            results.append(2)
            continue
        value = num
        idx = 0
        cnt = 1
        cnt_ = 1

        while value != 1:
            if value % prime_list[idx] == 0:
                cnt += 1
                value //= prime_list[idx]
            else:
                cnt_ *= cnt
                idx += 1
                cnt = 1
                
        cnt_ *= cnt
        results.append(cnt_)

    max_idx = results.index(max(set(results))) + start

    for i in starts:
        if i <= max_idx:
            answer.append(max_idx)
        else:
            i -= start
            max_value = max(set(results[i:]))
            answer.append(results[i:].index(max_value) + start + i)

    return answer

solution(8, [1,3,7])

#%%
def solution(e, starts):
    dp_count = [0] * (e + 1)
    for div in range(2, e + 1):
        for jump in range(0, e + 1, div):
            dp_count[jump] += 2

    for root in range(1, int(e ** 0.5) + 1):
        dp_count[root ** 2] += 1

    dp_div = [0] * (e + 1)
    max_count = 0
    for idx in range(e, 0, -1):
        if max_count <= dp_count[idx]:
            max_count = dp_count[idx]
            dp_div[idx] = idx
        else:
            dp_div[idx] = dp_div[idx + 1]

    return [dp_div[start] for start in starts]
