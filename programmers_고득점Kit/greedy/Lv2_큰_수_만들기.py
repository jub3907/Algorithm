#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    max_1 = max(set(number))
    
    while k != 0:
        num_set = {number[:i] + number[i + 1:] if number[i] != max_1 else '0' for i in range(len(number))}
        # num_set = set(filter(lambda x: (max_1 in x[:k+1]) or (max_2 in x[:k+1]) or (max_3 in x[:k+1]), num_set))
        number = max(num_set)
        k -= 1

    return number

solution("4177252841", 4)

#%%
def solution(number, k):
    number = list(number)

    while k != 0:
        front = set(number[:k + 2])
        min_index = front.index(min(front))
        number.pop(min_index)
        k -= 1
    
    answer = ''.join(number)
    return answer

# %%
def solution(number, k):
    num = number
    while k != 0:
        before_idx = 0
        idx = 0

        while True:
            if idx == len(number):
                number = number[k:]
                k = 0

            if number[idx] < number[idx + 1]:
                number = number[:idx] + number[idx + 1:]
                k -= 1
                break
            else:
                idx += 1
    
    return number

#%%
def solution(number, k):
    max_value = max(set(number))
    num = list(number)
    prev_current = 0
    while k != 0:
        # current = 0
        current = prev_current
        success = False

        while not success and current != len(num)-1:
            next = current + 1
            a = num[current] 
            b = num[next]
            if a == max_value:
                current += 1
                continue

            if a < b:
                success = True
            else:
                current += 1

        if success:
            num = num[:current] + num[current + 1 : ]
            if current != 0:
                prev_current = current - 1
            k -= 1
        else:
            num = num[:len(num) - k]
            k = 0
    
    return ''.join(num[k:])

# %%

def solution(number, k):
    answer = [] # Stack
    
    for num in number:
        if not answer:
            answer.append(num)
            continue
        if k > 0:
            while answer[-1] < num:
                answer.pop()
                k -= 1
                if not answer or k <= 0:
                    break
        answer.append(num)
        
    answer = answer[:-k] if k > 0 else answer
    return ''.join(answer)