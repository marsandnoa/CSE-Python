"""Test runner for HW6 Solution.

Author: Alan Weide
"""

import graph_sol as graph

vertices = {0, 1, 2, 3}
edges = {(0, 1), (0, 2), (1, 2), (2, 3)}

# not implemented
# try:
#     print("EdgelistGraph")
#     edge_g = graph.EdgelistGraph([(0, 1), (0, 2), (2, 1), (2, 3)])
#     print(f"{str(edge_g)  = }")
#     print(f"{repr(edge_g) = }")
#     print()
# except NotImplementedError as e:
#     print(f"Ignoring {repr(e)}")

try:
    print("MatrixGraph")
    matrix_g = graph.MatrixGraph([
                                    [False, True, True, False],
                                    [True, False, True, False],
                                    [True, True, False, True],
                                    [False, False, True, False]
                                ])
    print(f"{str(matrix_g)  = }")
    print(f"{repr(matrix_g) = }")
    print()
    print("TESTING REMOVAL ----------")
    matrix_g.remove_vertex(2)
    print(f"{str(matrix_g)  = }")
    print(f"{repr(matrix_g) = }")
    matrix_g.remove_vertex(1)
    print(f"{str(matrix_g)  = }")
    print(f"{repr(matrix_g) = }")
    matrix_g.add_vertex(2)
    print(f"{str(matrix_g)  = }")
    print(f"{repr(matrix_g) = }")
    matrix_g.add_vertex(3)
    print(f"{str(matrix_g)  = }")
    print(f"{repr(matrix_g) = }")

    matrix_g.add_edge((2,1))
    matrix_g.add_edge((3,2))
    print(f"{str(matrix_g)  = }")
    print(f"{repr(matrix_g) = }")

    matrix_g.remove_edge((2,1))
    matrix_g.remove_edge((3,2))
    print(f"{str(matrix_g)  = }")
    print(f"{repr(matrix_g) = }")

    print(matrix_g.degree(1))
    matrix_g.add_edge((2,1))
    print(matrix_g.degree(1))
    print(f"{str(matrix_g)  = }")
    print(f"{repr(matrix_g) = }")
except NotImplementedError as e:
    print(f"Ignoring {repr(e)}")

#not implemented
# try:
#     print("DictGraph")
#     dict_g = graph.DictGraph({0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2]})
#     print(f"{str(dict_g)  = }")
#     print(f"{repr(dict_g) = }")
#     print()
# except NotImplementedError as e:
#     print(f"Ignoring {repr(e)}")

# TODO: Add more test cases
