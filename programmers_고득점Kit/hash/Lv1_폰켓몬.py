#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    num_dict = {key : 0 for key in set(nums)}
    for num in nums:
        num_dict[num] += 1

    return_count = len(nums) / 2
    nums_count = len(num_dict.keys())
    if (nums_count < return_count):
        return nums_count
    else:
        return return_count

solution([3,3,3,2,2,4])