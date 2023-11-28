#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/42895
import operator
from functools import reduce

def solution(N, number):
    if set(str(number)) == {N}:
        return len(str(number))

    answer = 0
    i_dict = { 1 : {N} }
    max_value = N
    for i in range(2, 9):
        # i -> 2
        max_value += N * (10**(i - 1))
        i_dict[i] = {max_value}
        i_set = {(i - j, j) for j in range(1, i)}
        for m, n in i_set:
            m_value_set = i_dict[m]
            n_value_set = i_dict[n]
            for m_value in m_value_set:
                for n_value in n_value_set:
                    i_dict[i].add(m_value * n_value)
                    i_dict[i].add(m_value + n_value)
                    i_dict[i].add(m_value - n_value)
                    if n_value != 0:
                        i_dict[i].add(m_value // n_value)

    # print(reduce(operator.or_, i_dict.values()))
    
    for key, value_set in i_dict.items():
        # print(key, sorted(list(value_set)))
        if number in value_set:
            answer = key
            break
    

    return answer if answer != 0 else -1

solution(2, 11)
# %%
