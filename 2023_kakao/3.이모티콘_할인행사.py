#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/150368

# n명의 사용자에게 m개를 할인
# 할인율은 10 20 30 40

import itertools

def get_prices(emoticons, percents, users):
    prices = [0 for _ in range(len(users))]
    for e, p in zip(emoticons, percents):
        for idx, user in enumerate(users):
            standard = user[0]
            if standard <= p:
                prices[idx] += int((e // 100) * (100 - p))

    return prices
    
def solution(users, emoticons):
    max_cnt = 0
    max_price = 0
    for product in itertools.product((40, 30, 20, 10), repeat = len(emoticons)):
        cnt = 0
        total_price = 0
        prices = get_prices(emoticons, product, users)
        for idx, price in enumerate(prices):
            if users[idx][1] <= price:
                cnt += 1
            else:
                total_price += price

        if max_cnt < cnt:
            max_cnt = cnt
            max_price = total_price
        elif max_cnt == cnt and max_price < total_price:
            max_price = total_price


    return [max_cnt, max_price]

# solution([[40, 10000], [25, 10000]], 	[7000, 9000])

solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900])