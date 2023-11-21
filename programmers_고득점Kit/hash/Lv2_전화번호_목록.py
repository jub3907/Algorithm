#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    phone_dict = {i : set() for i in range(1, 21)}
    for phone in phone_book:
        phone_dict[len(phone)].add(phone)

    checked = set()
    for phone in phone_book:
        for i in range(0, len(phone)):
            tmp = phone[:i]
            if tmp and tmp not in checked:
                if tmp in phone_dict[len(tmp)]:
                    return False
                else:
                    checked.add(tmp)
    
    return True

solution(["12","123","1235","567","88"])

# %%
