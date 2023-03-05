import sys
import threading
import numpy


def compute_height(n, vecaki) : 
    sakne = None
    position =[[]for_in range(n)]
    for i in range(n):
        if vecaki[i] == -1
        sakne = i
        else:
            position[vecaki[i]].append(i)



def max_height(b):
    if not position[b]:
        return 1
        else:
            max_child_height = max(max_height(berni) for berni in position[b])
            return max_child_height + 1
return max_height(sakne)

        


def main():
    text = input("Enter I or F: ")
    if "F" in text:
        filename = input()
        file_path = f"./text/{filename}"
        if "a" not in filename:
            try:
                with open(file_path) as f:
                    n =int(f.readline())
                    vecaki = list(map(int, f.readline().split()))
            except Exception as e:
                print("Error:",str(e))
                return
        else:
            print("error: invalid filname")
            return
    elif "I" in text:
        n = int(input())
        vecaki = list(map(int,input().split()))

  

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=lambda: print(compute_height(n, vecaki))).start()

if _name_ == "__main__":
    main()