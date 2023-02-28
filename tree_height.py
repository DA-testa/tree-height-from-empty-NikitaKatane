import sys
import threading
import numpy as np


def compute_height(n, parents) : 
    tree = [[] for _ in range(n)]
    for i in range(n):
        if parents[i] == -1:
            root = i 
        else:
            tree[parents[i]].append(i)

    heights = [-1] *  n
    def compute_height_recursive(node):
        if not tree[node]:
            heights[node] = 0
            return 0
        max_child_height = max([compute_height_recursive(child) for  child in tree[node]])
        heights[node] =  max_child_height + 1
        return heights[node]

    compute_height_recursive(root)
    return max(heights) +  1


def main():
    n = int(input())
    parents = np.fromstring(input(), dtype=int, sep=' ')
    print(compute_height(n, parents)) 

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()