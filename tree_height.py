import sys
import threading
import numpy


def compute_height(n, parents):
    root = -1
    position = [[] for _ in range(n)]
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            position[parents[i]].append(i)
    return root, position


def max_height(root, position):
    if not position[root]:
        return 1
    else:
        max_child_height = max(max_height(children, position) for children in position[root])
        return max_child_height + 1


def main():
    text = input("Enter I or F: ")
    if "F" in text:
        filename = input()
        file_path = f"./text/{filename}"
        if "a" not in filename:
            try:
                with open(file_path) as f:
                    n = int(f.readline())
                    parents = list(map(int, f.readline().split()))
                    root, position = compute_height(n, parents)
            except Exception as e:
                print("Error:", str(e))
                return
        else:
            print("error: invalid filname")
            return
    elif "I" in text:
        n = int(input())
        parents = list(map(int, input().split()))
        root, position = compute_height(n, parents)

    sys.setrecursionlimit(10 ** 7)
    threading.stack_size(2 ** 27)
    threading.Thread(target=lambda: print(max_height(root, position))).start()


if __name__ == "__main__":
    main()
