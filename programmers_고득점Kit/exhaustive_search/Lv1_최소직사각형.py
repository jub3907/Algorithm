#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    answer = 0
    v, h, size = 0, 0, 0
    for tmp_v, tmp_h in sizes:
        if tmp_v <= v and tmp_h < h:
            continue
        elif tmp_v <= h and tmp_h <= v:
            continue
        else:
            if max(v, tmp_v) * max(h, tmp_h) > max(v, tmp_h) * max(h, tmp_v):
                v = max(v, tmp_h)
                h = max(h, tmp_v)
            else:
                v = max(v, tmp_v)
                h = max(h, tmp_h)
    return v * h

solution([[60, 50], [30, 70], [60, 30], [80, 40]])
solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])
# %%
