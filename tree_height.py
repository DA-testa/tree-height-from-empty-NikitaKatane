import sys
import threading
import numpy as np


def compute_height(n, parents):
    tree = [[] for _ in range(n)]
    root = None
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            tree[parents[i]].append(i)

    def compute_height_recursive(node):
        if not tree[node]:
            return 0
        max_child_height = max([compute_height_recursive(child) for child in tree[node]])
        return max_child_height + 1

    return compute_height_recursive(root)


def main():
    n = int(input())
    parents = np.fromstring(input(), dtype=int, sep=' ')
    print(compute_height(n, parents)) 

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()