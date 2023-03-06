import sys
import threading

def compute_height(n, parents):
    root = None 
    position = [[] for _ in range(n)]
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            position[parents[i]].append(i)
    return root, position

def max_height(root, position):
    height = 1 
    if not position[root]:
        return height
    else:
        for child in position[root]:
            height = max(height, 1 + max_height(child, position))
        return height

def main():
    text = input("Enter I or F: ")
    if "I" in text:
        n = int(input())
        parents = list(map(int, input().split()))
        print(max_height(*compute_height(n, parents)))
    elif "F" in text:
        filename = input()
        file = "./text/" + filename
        if "a" not in filename:
            try:
                with open(file) as f:
                    n = int(f.readline())
                    parents = list(map(int, f.readline().split()))
                    print(max_height(*compute_height(n, parents)))
            except Exception as e:
                print("Error:", str(e))
        else:
            print("Error: invalid filename")

sys.setrecursionlimit(10 ** 7)
threading.stack_size(2 ** 27)
threading.Thread(target=main).start()
