# python3

import sys
import threading
import numpy

class Node:
    def _int_(self,value):
        self.value =value
        self.children = []

def compute_height(n, parents):
    nodes = [Node(i) for i in range (n)]
    root = None
    for i in range(n):
        if parents[i] == -1
        root = nodes[i]
        else:
            nodes.[parents].children.append(nodes[i])


def dfs(node):
    if not node.children:
        return 0 
        return 1 + max(dfs(child) for child in node.children)
        
        return dfs(root)
        
def main():
    n = int(input())
    parents = list(map(int,input().split()))
    print(compute_height(n, parents))
    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))