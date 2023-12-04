#%%

min_value = float('inf')

def getDiff(word_a, word_b):
    diff = 0
    for a, b in zip(word_a, word_b):
        if a != b:
            diff += 1
    return diff

def dfs(words_dict, current, target, visited, count):
    global min_value
    if current == target:
        if count < min_value:
            min_value = count
            return

    for next in words_dict[current]:
        if next not in visited:
            next_visited = visited.copy()
            next_visited.append(next)
            dfs(words_dict, next, target, next_visited, count + 1)

def solution(begin, target, words):
    global min_value
    if target not in words:
        return 0
    
    words_dict = {word : [] for word in words}
    words_dict[begin] = []

    for key in words:
        for word in words:
            if key == word:
                continue
            if getDiff(key, word) == 1:
                words_dict[key].append(word)
    
    for word in words:
        if begin == word:
            continue
        if getDiff(begin, word) == 1:
            words_dict[begin].append(word)

        
    dfs(words_dict, begin, target, [begin], 0)

    return min_value if min_value != float('inf') else 0


solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
# %%
