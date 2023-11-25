#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    total_size = brown + yellow
    pers = set()
    for i in range(1, (total_size // 2) + 2):
        if total_size % i == 0 and i >= total_size // i:
            pers.add((i, total_size // i))

    for v, h in pers:
        if v <= 2 or h <= 2 or v < h:
            continue

        tmp_b = 2 * (v + h) - 4
        tmp_y = (v - 2) * (h - 2)

        if tmp_b == brown and tmp_y == yellow:
            return [v, h]

solution(24, 24)
# %%
