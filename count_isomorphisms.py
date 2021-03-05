from colors_copy import *
import copy


def count_isomorphisms(g, h):
    union = union_graphs(g, h)
    D = []
    I = []
    num = _count_isomorphisms(D, I, union)
    return num


def _count_isomorphisms(D, I, union):
    color_graph(union, D, I)
    with open('colorful.dot', 'w') as f:
        write_dot(union, f)
    balance_analysis, dict_g, dict_h = is_balanced(union)

    if balance_analysis == -1:
        return 0
    if balance_analysis == -2:
        return 1

    num = 0
    x = dict_g[balance_analysis][0]
    for y in dict_h[balance_analysis]:
        D_copy = D[:]
        D_copy.append(x)
        I_copy = I[:]
        I_copy.append(y)
        num = num + _count_isomorphisms(D_copy, I_copy, union)
        # print('hello')
        # print(D)
        # print(I)
        # D.pop()
        # I.pop()
        # print('hello2')
        # print(D)
        # print(I)
        # print('hello3')
    return num


# return -1 if unbalanced
# return -2 if bijection
# return color number to change otherwise
def is_balanced(union):
    bijection = -2
    dict_g, dict_h = coldict(union)
    for key in dict_g:
        if not (key in dict_h):
            return -1, dict_g, dict_h
        if len(dict_g[key]) != len(dict_h[key]):
            return -1, dict_g, dict_h
        if len(dict_g[key]) >= 2:
            bijection = key

    return bijection, dict_g, dict_h


def union_graphs(g, h):
    return g.__add__(h)


def preprocessing(g, h):
    if len(g) != len(h):
        return False
    return count_isomorphisms(g, h)


def coldict(union):
    dict_g = {}
    dict_h = {}

    for i in range(0, len(union) // 2):
        dict_g[union.vertices[i].colornum] = []

    for i in range(0, len(union) // 2):
        dict_g[union.vertices[i].colornum].append(union.vertices[i])

    for i in range(len(union) // 2, len(union)):
        dict_h[union.vertices[i].colornum] = []

    for i in range(len(union) // 2, len(union)):
        dict_h[union.vertices[i].colornum].append(union.vertices[i])
    return dict_g, dict_h


if __name__ == '__main__':
    name_file = 'torus144.grl'
    with open(name_file) as f:
        L = load_graph(f, read_list=True)

    g = L[0][9]
    h = L[0][5]

    print(preprocessing(g, h))
