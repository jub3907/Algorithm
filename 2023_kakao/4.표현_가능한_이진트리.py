#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/150367

def get_bin(value):
    return str(bin(value))[2:]

def solution(numbers):
    answer = []
    for number in numbers:
        bin_number = get_bin(number)
        print(bin_number)
    return answer

solution([7, 42, 5])
solution([63, 111, 95])
# %%
