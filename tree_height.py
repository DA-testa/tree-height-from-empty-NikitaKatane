class Node:
    def _init_(self, val):
        self.val = val
        self.berni = [] 


def musu_koks(n, vecaki) :
    nodes = [Node(i) for i in range(n)]
    sakne = None
    for i, p in  enumerate(vecaki):
        if p == -1:
            sakne = nodes[i]
        else:
            nodes[p].berni.append(nodes[i])
    return sakne
    

def dzilums(sakne):
    if sakne  is None :
        return 0
    dzil = 1
    for mazie in sakne.berni:
        dzil =  max(dzil, 1 + dzilums(mazie))
    return dzil 
    

n = int(input())
vecaki = list(map(int, input().split()))
sakne = musu_koks(n, vecaki) 
print(dzilums(sakne))