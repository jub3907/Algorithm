#%%
# https://velog.io/@error_io/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%9C%A0%EC%82%AC-%EC%B9%B8%ED%86%A0%EC%96%B4-%EB%B9%84%ED%8A%B8%EC%97%B4-Lv.-2-Python
def solution(n, l, r):
    answer = 0
    for l in range(l-1, r):
        if is_one(l):
            answer += 1
    return answer

def is_one(l):
    while l >= 5:
        if (l - 2) % 5 == 0:
            return False
        l //= 5

    return l != 2