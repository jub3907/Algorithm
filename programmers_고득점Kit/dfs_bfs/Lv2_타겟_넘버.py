#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/43165
from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.value)


def solution(numbers, target):
    global answer
    def create_tree(node, index):
        node_left = Node(-numbers[index])
        node_right = Node(numbers[index])
        node.left = node_left
        node.right = node_right

        if index == len(numbers) - 1:
            return
        
        create_tree(node.left, index + 1)
        create_tree(node.right, index + 1)



    def dfs(node, value, target):
        global answer
        if node.left == None:
            if value + node.value == target:
                answer += 1
        else:
            dfs(node.left, value + node.value, target)
            dfs(node.right, value + node.value, target)

    answer = 0
    root = Node(0)
    create_tree(root, 0)

    dfs(root, 0, target)


    return answer

solution([1, 1, 1, 1, 1]	, 3)
# %%
