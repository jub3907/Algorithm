#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/152995
def solution(scores):
    main = scores[0]
    main_rank = -1
    main_index = 0
    scores = sorted(scores, key = lambda x: x[0] + x[1], reverse=True)
    new = []
    prev = -1
    rank = 1
    bulk = 0

    for idx, value in enumerate(scores):
        flag = False
        a, b = value
        for i, j in scores[:idx]:
            if a < i and b < j:
                flag = True
                break
        if flag:
            new.append((-1, a, b))
            continue

        if a + b == prev:
            bulk += 1
        else:
            rank += bulk
            bulk = 1

        if a == main[0] and b == main[1]:
            main_rank = rank
            main_index = idx

        new.append((rank, a, b))
        prev = a + b

    for idx in range(main_index + 1):
        _, a, b = new[idx]
        target_a, target_b = main
        if target_a < a and target_b < b:
            return -1
    
    return main_rank

# solution([[2,2],[1,4],[3,2],[3,2],[2,1]])
# solution([[3,2],[2,3],[3,2],[2,3]])
# solution([[2,1],[2,2],[2,3],[3,1]])
# solution([[3, 1], [2, 5], [2, 10]])
solution([[7, 1], [6, 6], [5, 4], [5, 4], [6, 6]])
# %%

def solution(scores):
    main = scores[0]
    main_rank = -1
    main_index = 0
    scores = sorted(scores, key = lambda x: x[0] + x[1], reverse=True)
    new = []
    prev = -1
    rank = 1
    bulk = 0
    a_break_set, b_break_set = set(), set()
    break_set = set()
    
    for idx, value in enumerate(scores):
        flag = False
        a, b = value

        if (a, b) in break_set:
            new.append((-1, a, b))
            continue

        if a_break_set:
            if a <= max(a_break_set) or b <= max(b_break_set):
                for i, j in scores[:idx]:
                    if a < i and b < j:
                        flag = True
                        a_break_set.add(a)
                        b_break_set.add(b)
                        break_set.add((a, b))
                        break
        else:
            for i, j in scores[:idx]:
                if a < i and b < j:
                    flag = True
                    a_break_set.add(a)
                    b_break_set.add(b)
                    break_set.add((a, b))
                    break

        if flag:
            new.append((-1, a, b))
            continue

        if a + b == prev:
            bulk += 1
        else:
            rank += bulk
            bulk = 1

        if a == main[0] and b == main[1]:
            main_rank = rank
            main_index = idx

        new.append((rank, a, b))
        prev = a + b

    for idx in range(main_index + 1):
        _, a, b = new[idx]
        target_a, target_b = main
        if target_a < a and target_b < b:
            return -1
    
    return main_rank

solution([[7, 1], [6, 6], [5, 4], [5, 4], [6, 6], [1, 1]])
# %%
