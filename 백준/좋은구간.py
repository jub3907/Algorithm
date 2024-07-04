#%%
# 
import sys
L = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
n = int(sys.stdin.readline())
nums.sort()  

if n in nums:
    print(0)
else:
    min = 0
    max = 0
    for num in nums:            # 배열중에서 n과 가장 근접한 두 수를 구한다.
        if num < n:     
            min = num
        elif num > n and max == 0:
            max = num
    max -= 1                    # 1과 7사이에 n이 2이면 1과 7은 제외
    min += 1
    print((n-min)*(max-n+1) + (max-n))