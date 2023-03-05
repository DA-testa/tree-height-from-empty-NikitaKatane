import sys
import threading


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


class Tree:
    def __init__(self, n, parents):
        self.nodes = [Node(i) for i in range(n)]
        for i in range(n):
            parent = parents[i]
            if parent == -1:
                self.root = self.nodes[i]
            else:
                self.nodes[parent].children.append(self.nodes[i])

    def max_height(self):
        def dfs(node):
            if not node.children:
                return 1
            else:
                max_child_height = max(dfs(child) for child in node.children)
                return max_child_height + 1

        return dfs(self.root)


def main():
    text = input("Enter I or F: ")
    if text == "I":
        n = int(input())
        parents = list(map(int, input().split()))
        tree = Tree(n, parents)
    elif text == "F":
        filename = input()
        file_path = f"./text/{filename}"
        if "a" not in filename:
            try:
                with open(file_path) as f:
                    n = int(f.readline())
                    parents = list(map(int, f.readline().split()))
                    tree = Tree(n, parents)
            except Exception as e:
                print("Error:", str(e))
                return
        else:
            print("Error: invalid filename")
            return

    sys.setrecursionlimit(10 ** 7)
    threading.stack_size(2 ** 27)
    threading.Thread(target=lambda: print(tree.max_height())).start()


if __name__ == "__main__":
    main()
