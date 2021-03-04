from colors import *


def count_isomorphisms(g, h, union):
    color_graph(union)
    return balanced(g, h, union)

def balanced(g, h, union):
    dict1, dict2 = coldict(union)
    print(dict1)
    print(dict2)
    for keys in dict1:
        if not (keys in dict2):
            return False
        if dict1[keys] != dict2[keys]:
            return False

    return True

def union_graphs(g, h):
    return g.__add__(h)


def preprocessing(g, h):
    if len(g) != len(h):
        return False
    union = union_graphs(g, h)
    return count_isomorphisms(g, h, union)

def coldict(union):
    dictg={}
    dictv={}
    color_graph(union)

    for v in union.vertices[0:len(union)//2]:
        dictg[v.colornum] = 0
    for v in union.vertices[0:len(union)//2]:
        dictg[v.colornum] = dictg[v.colornum]+1
    for v in union.vertices[len(union)//2::]:
        dictv[v.colornum] = 0
    for v in union.vertices[len(union)//2::]:
        dictv[v.colornum] = dictv[v.colornum]+1

    return dictg, dictv

if __name__ == '__main__':
    name_file = 'cref9vert_4_9.grl'
    with open(name_file) as f:
        L = load_graph(f, read_list=True)

    g = L[0][1]
    h = L[0][0]

    print(preprocessing(g, h))