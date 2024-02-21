#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/12904
def isPalindrome(x):
    if x==x[::-1]:
        return True
    
def solution(s):
    MAX=0
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            if isPalindrome(s[i:j]):
                if MAX<len(s[i:j]):
                    MAX=len(s[i:j])
    return MAX
