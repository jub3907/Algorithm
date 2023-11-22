#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/12909

#%%
MAX_STACK_SIZE = 100000


class Stack:
    def __init__(self):
        self.arr = [None] * MAX_STACK_SIZE
        self.top = -1

    def is_full(self):
        if self.top >= MAX_STACK_SIZE - 1:
            return True
        else:
            return False

    def push(self, value):
        if self.is_full():
            return None
        else:
            self.top += 1
            self.arr[self.top] = value

    def is_empty(self):
        if self.top < 0:
            return True
        else:
            return False

    def pop(self):
        if self.is_empty():
            return None
        else:
            value = self.arr[self.top]
            self.top -= 1
            return value


def solution(s):
    stack = Stack()

    for brace in s:
        if brace == "(":
            stack.push(1)
        else:
            pop = stack.pop()
            if pop == None:
                return False
    if stack.is_empty():
        return True
    else:
        return False