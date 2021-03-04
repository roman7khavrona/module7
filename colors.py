from graph import *
from graph_io import load_graph, save_graph, write_dot
from collections import Counter


def color_graph(graph):
    # with open(name_file) as f:
    #     L = load_graph(f, read_list=True)
    #
    #
    # graph = L[0][0]
    # graph = graph.__add__(L[0][3])


    for v in graph.vertices:
        v.colornum = 0

    i = 0
    can_update = True
    old_color_length = 0
    while can_update:
        can_update = False
        # print("iteration:")
        # print(i)
        to_be_processed = graph.vertices
        colors = {}
        current_color = 0
        change_happened = False
        for active_vertex in graph.vertices:
            if active_vertex in to_be_processed:
                # print("active_vertex")
                # print(active_vertex)
                colors[current_color] = [active_vertex]
                to_be_processed.remove(active_vertex)
                for other_vertex in graph.vertices:
                    if other_vertex in to_be_processed:
                        if active_vertex.degree == other_vertex.degree:
                            if matching_neighbourhoods(active_vertex, other_vertex):
                                colors[current_color].append(other_vertex)
                                to_be_processed.remove(other_vertex)
            current_color += 1
        for color in colors:
            for vertex in colors[color]:
                vertex.colornum = color

        # print("old color length:")
        # print(old_color_length)
        # print("current color length:")
        # print(len(colors))

        if old_color_length != len(colors):
            can_update = True

        old_color_length = len(colors)
        i+=1

    with open('colorful.dot', 'w') as f:
        write_dot(graph, f)

def matching_neighbourhoods(vertex1, vertex2):
    return (Counter([vertex.colornum for vertex in vertex1.neighbours]) == Counter(
        [vertex.colornum for vertex in vertex2.neighbours]))


# if __name__ == '__main__':
# #     # color_graph('colorref_smallexample_6_15.grl')
#     color_graph('cref9vert_4_9.grl')
