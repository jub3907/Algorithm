#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/43164

result = []

def dfs(target_count, ticket_dict, ticket_dict_count, visited, current, course):
    global result

    if len(visited) == target_count:
        result.append(course)
        return
    
    if current in ticket_dict.keys():
        for next in ticket_dict[current]:
            if course.count((current, next)) != ticket_dict_count[(current, next)]:
                next_v = visited.copy()
                next_v.append((current, next))

                next_c = course.copy()
                next_c.append(next)


                dfs(target_count, ticket_dict, ticket_dict_count, next_v, next, next_c)




def solution(tickets):
    ticket_dict = {}
    ticket_dict_count = {}
    cnt = 0
    for f, t in tickets:
        if (f, t) in ticket_dict_count.keys():
            ticket_dict_count[(f, t)] += 1
        else:
            ticket_dict_count[(f, t)] = 1
        cnt += 1
        if f in ticket_dict.keys():
            ticket_dict[f].append(t)
        else:
            ticket_dict[f] = [t]

    start = "ICN"
    dfs(cnt, ticket_dict, ticket_dict_count, list(), start, [start])

    return sorted(result)[0]

# solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
solution([["ICN", "AAA"], ["ICN", "CCC"], ["CCC", "DDD"], ["AAA", "BBB"], ["AAA", "BBB"], ["DDD", "ICN"], ["BBB", "AAA"]])
# %%

def solution(tickets):

    def dfs(departure: str, path: list):
        if len(path) == n + 1:
            return path

        if airports.get(departure):
            for entrance in airports.get(departure):
                if visited[departure][entrance] == 0:
                    continue

                visited[departure][entrance] -= 1
                new_path = path + [entrance]
                result = dfs(entrance, new_path)
                if result:
                    return result
                visited[departure][entrance] += 1


    n = len(tickets)
    tickets.sort(key = lambda x:x[1])
    answer = []
    airports = dict()
    visited = dict()

    for departure, entrance in tickets:
        if airports.get(departure):
            airports[departure].append(entrance)
        else:
            airports.setdefault(departure, [entrance])

    for departure, entrances in airports.items():
        for entrance in entrances:
            if visited.get(departure):
                if visited[departure].get(entrance):
                    visited[departure][entrance] += 1
                else:
                    visited[departure][entrance] = 1
            else:
                visited.setdefault(departure, {entrance: 1})

    answer = dfs("ICN", ["ICN"])
    return answer