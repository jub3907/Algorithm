#%%
# https://school.programmers.co.kr/learn/courses/30/lessons/42892

from sys import setrecursionlimit

setrecursionlimit(10000)

class Node(object):
    def __init__(self, info):
        self.num = info[2]
        self.pos = info[:2]
        self.left = None
        self.right = None
        
def solution(nodeinfo):
    answer = [[]]
    for idx in range(len(nodeinfo)):
        nodeinfo[idx].append(idx+1)
    
    nodeinfo.sort(key=lambda x :(-x[1],x[0]))
    tree = Node(nodeinfo[0])
    
    for info in nodeinfo[1:]:
        add_node(tree,info)
    
    return [pre_order(tree),post_order(tree)]

def pre_order(curr):
    path = [curr.num]
    if curr.left:
        path += pre_order(curr.left)
    if curr.right:
        path += pre_order(curr.right)
    return path

def post_order(curr):
    path = []
    if curr.left:
        path += post_order(curr.left)
    if curr.right:
        path += post_order(curr.right)
    path.append(curr.num)
    return path
    
def add_node(parent,info):
    if parent.pos[0] > info[0]:
        if parent.left:
            add_node(parent.left,info)
        else:
            parent.left = Node(info)
    else:
        if parent.right:
            add_node(parent.right,info)
        else:
            parent.right = Node(info)

#%%

from collections import defaultdict
import sys
sys.setrecursionlimit(1005)
MAX = 100001
MIN = -1
TREE_DEPTH = 0

def solution(nodeinfo):
    global TREE_DEPTH

    pre_tree = defaultdict(list)
    post_tree = defaultdict(list)
    level = set()

    for i in range(len(nodeinfo)):
        x, y = nodeinfo[i]
        pre_tree[y].append((x, i+1))
        post_tree[y].append((x, i+1))
        level.add(y)

    for i in level:
        pre_tree[i].sort(reverse=True)
        post_tree[i].sort(reverse=True)

    level = sorted(list(level), reverse=True)
    TREE_DEPTH = len(level)
    
    preorder = []
    pre_order(MIN, MAX, 0, preorder, pre_tree, level)
    postorder = []
    post_order(MIN, MAX, 0, postorder, post_tree, level)

    return [preorder, postorder]


def pre_order(left, right, depth, result, tree, level):
    if depth == TREE_DEPTH:
        return
    if len(tree[level[depth]]) <= 0:
        return
    if not (left < tree[level[depth]][-1][0] < right):
        return
    
    x, index = tree[level[depth]].pop()
    result.append(index)
    pre_order(left, x, depth+1, result, tree, level)
    pre_order(x, right, depth+1, result, tree, level)


def post_order(left, right, depth, result, tree, level):
    if depth == TREE_DEPTH:
        return
    if len(tree[level[depth]]) <= 0:
        return
    if not (left < tree[level[depth]][-1][0] < right):
        return
    
    x, index = tree[level[depth]].pop()
    post_order(left, x, depth+1, result, tree, level)
    post_order(x, right, depth+1, result, tree, level)
    result.append(index)