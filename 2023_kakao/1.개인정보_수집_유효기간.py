#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/150370

def solution(today, terms, privacies):
    terms_dict = {}
    for term in terms:
        i, j = term.split()
        terms_dict[i] = int(j)

    year, month, day = list(map(int, today.split(".")))
    answer = []
    print(year, month, day)
    for index, privacy in enumerate(privacies):
        privacy_date, privacy_term = privacy.split()
        added = terms_dict[privacy_term]

        y, m, d = list(map(int, privacy_date.split(".")))
        m += added
        while m > 12:
            m -= 12
            y += 1


        print(y, m, d)
        if y < year or (y == year and m < month) or (y == year and m == month and d <= day):
            answer.append(index + 1)

    return answer


solution("2022.05.19", ["A 6", "B 12", "C 3"],  ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])

# %%

