#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/84512
from itertools import product

def solution(word):
    # 만들 수 있는 단어 중복 순열로 생성
    products = list()
    words = ['A','E','I','O','U']

    for j in range(1, 6):
        products += list(product(words, repeat = j))

    word_products = list(map(lambda x: ''.join(x), sorted(products)))
    return word_products.index(word) + 1

solution("EIO")

# %%
