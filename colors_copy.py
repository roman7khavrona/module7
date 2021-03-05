from graph import *
from graph_io import load_graph, save_graph, write_dot
from collections import Counter

def color_graph(graph, D, I):

    for v in graph.vertices:
        v.colornum = 0

    current_color_predefined = 1
    for j in range(len(D)):
        D[j].colornum = current_color_predefined
        I[j].colornum = current_color_predefined
        current_color_predefined = current_color_predefined + 1

    # can_update = True
    # old_color_length = 0
    # start_color = current_color_predefined
    # while can_update:
    #     can_update = False
    #     new_coloring = {}
    #
    #     for active_vertex in graph.vertices:
    #         for other_vertex in graph.vertices:
    #             if active_vertex.label != other_vertex.label:
    #                 continue
    #             else:
    #                 if active_vertex.colornum == other_vertex.colornum and matching_neighbourhoods(active_vertex, other_vertex):
    #                     if active_vertex.colornum in new_coloring:
    #                         if not (active_vertex in new_coloring[active_vertex.colornum]):
    #                             new_coloring[active_vertex.colornum].append(active_vertex)
    #                         if not (other_vertex in new_coloring[active_vertex.colornum]):
    #                             new_coloring[active_vertex.colornum].append(other_vertex)
    #                     else:
    #                         new_coloring[active_vertex.colornum] = [active_vertex, other_vertex]
    #                 else:

    can_update = True
    old_color_length = 0
    while can_update:
        can_update = False
        to_be_processed = graph.vertices
        colors = {}
        current_color = 0
        for active_vertex in graph.vertices:
            if active_vertex in to_be_processed:
                colors[current_color] = [active_vertex]
                to_be_processed.remove(active_vertex)
                for other_vertex in graph.vertices:
                    if other_vertex in to_be_processed:
                        if active_vertex.colornum == other_vertex.colornum and active_vertex.degree == other_vertex.degree:
                            if matching_neighbourhoods(active_vertex, other_vertex):
                                colors[current_color].append(other_vertex)
                                to_be_processed.remove(other_vertex)
            current_color += 1
        for color in colors:
            for vertex in colors[color]:
                vertex.colornum = color

        if old_color_length != len(colors):
            can_update = True

        old_color_length = len(colors)

def matching_neighbourhoods(vertex1, vertex2):
    return vertex1.degree == vertex2.degree and (Counter([vertex.colornum for vertex in vertex1.neighbours]) == Counter(
        [vertex.colornum for vertex in vertex2.neighbours]))

