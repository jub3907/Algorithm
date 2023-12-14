#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/161988
# https://shoark7.github.io/programming/algorithm/4-ways-to-get-subarray-consecutive-sum
# 수열의 구간합 최대 값 : 
    # 배열 arr에 대해, f(i)는 인덱스 i를 오른쪾 끝으로 갖는 구간의 최대 합.
    # 이 때, 다음과 같은 식이 성립한다.
        # f(i) = max(0, f(i - 1)) + arr[i]
        # if i == 0, f(i) = arr[i]
def solution(sequence):
    
    pulse_with_plus = [1, -1] * (len(sequence) // 2) + [1] * (len(sequence) % 2)
    pulse_with_minus = [-1, 1] * (len(sequence) // 2) + [-1] * (len(sequence) % 2)
    
    sequence_with_plus = [i * j for i, j in zip(sequence, pulse_with_plus)]
    sequence_with_minus = [i * j for i, j in zip(sequence, pulse_with_minus)]
    
    cache = [None] * len(sequence)
    cache_minus = [None] * len(sequence)
    cache[0] = sequence_with_plus[0]
    cache_minus[0] = sequence_with_minus[0]

    for i in range(1, len(sequence)):
        cache[i] = max(0, cache[i - 1]) + sequence_with_plus[i]
        cache_minus[i] = max(0, cache_minus[i - 1]) + sequence_with_minus[i]

    return max(set(cache + cache_minus))
