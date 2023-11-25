#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/42839

import itertools

def solution(numbers):
    pers = set()
    for i in range(1, len(numbers) + 1):
        pers = pers.union(set(itertools.permutations(list(numbers), i)))

    pers = set(map(lambda x: int(''.join(x)), pers))
    max_pers = max(pers)

    n = max_pers
    sieve = [False, False] + [True] * (n - 1)
    primes = set()

    for i in range(2,n+1):
        if sieve[i]:
            primes.add(i)
            for j in range(2 * i, n + 1, i):
                sieve[j] = False

    prime_pers = set(filter(lambda x: x in primes, pers))

    return len(prime_pers)
