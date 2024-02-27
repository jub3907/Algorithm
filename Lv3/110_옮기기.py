#%%
#https://school.programmers.co.kr/learn/courses/30/lessons/77886

def solution(s):
    answer = []
    for arr in s:
        stack, num110, i = [], 0, 0
        while i < len(arr):
            if arr[i] == '0':
                if len(stack) >= 2 and stack[-2] == '1' and stack[-1] == '1':
                    stack.pop()
                    stack.pop()
                    num110 += 1
                    i += 1
                else:
                    stack.append(arr[i])
                    i += 1
            else:
                stack.append(arr[i])
                i += 1
                
        stack = ''.join(stack[::-1])
        idx = stack.find('0')
        
        if idx != -1:
            res = stack[:idx] + '011' * num110 + stack[idx:]
        else:
            res = stack + '011' * num110
        answer.append(''.join(res[::-1]))
        
    return answer