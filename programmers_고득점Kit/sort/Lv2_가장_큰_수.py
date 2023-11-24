#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    nums = []
    answer = ''
    for number in numbers:
        str_value = str(number)
        formatting = str_value + (4 - len(str_value)) * str_value[0]
        formatting_2 = str_value + (4 - len(str_value)) * str_value[-1]
        nums.append([number, formatting, formatting_2])

    nums = sorted(nums, key = lambda x: (x[1], x[2]), reverse= True)
    while nums:
        answer += str(nums.pop(0)[0])
    
    if answer and answer[0] == '0':
        return '0'
    return answer

solution([0,0,0,0])