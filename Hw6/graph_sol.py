"""Template for the graph section of HW 6.

CSE 4256
Author: Noah Marsteller
Due: Feb 27, 2022
"""
from abc import ABC, abstractmethod

class Graph(ABC):
    """Abstract class representing a graph.

    A graph is modeled as a pair of sets (vertices, edges).

    Each element of edges is a tuple (v1, v2) where v1 and v2 are both in vertices.
    """

    @abstractmethod
    def __repr__(self):
        """Returns a string representation of self using the underlying representation."""

        return f"{type(self)}:{str(self)}"

    @property
    @abstractmethod
    def vertices(self) -> set:
        """A set of all vertices in self."""

    @property
    @abstractmethod
    def edges(self):
        """A set of all edges in self.

        Each edge is a collection of two vertices.
        """

    @abstractmethod
    def degree(self, vertex) -> int:
        """Returns the degree of vertex.

        Returns the number of edges incident on vertex.
        """

    @abstractmethod
    def adjacent_to(self, vertex):
        """Returns a set of all vertices in self adjacent to vertex."""

    @abstractmethod
    def add_vertex(self, vertex):
        """Adds vertex to self.vertices."""

    @abstractmethod
    def add_edge(self, edge):
        """Adds edge to self.edges.

        Assumes: edge[0] and edge[1] are both in self.vertices.
        """

    @abstractmethod
    def remove_vertex(self, vertex):
        """Removes vertex and all incident edges from self.

        Assumes: vertex in self.vertices.
        """

    @abstractmethod
    def remove_edge(self, edge):
        """Removes edge from self, leaving the endpoints in self.vertices.

        Assumes: edge in self.edges.
        """

    # Non-abstract methods

    def __eq__(self, other):
        """Returns true iff self.vertices is exactly the same as other.vertices and self.edges is
            exactly the same as other.edges."""

        return self.vertices == other.vertices and self.edges == other.edges

    def __str__(self):
        """Returns a string representation of self as a pair of sets."""

        vertex_set = set(self.vertices)
        edge_set = {tuple(edge) for edge in self.edges}
        return f"({vertex_set}, {edge_set})"

    def __imul__(self, vertex):
        """Adds vertex to self.

        Called by the *= operator.
        """

        self.add_vertex(vertex)

    def __iadd__(self, edge):
        """Adds edge to self.

        Called by the += operator.
        """

        self.add_edge(*edge)

    def __itruediv__(self, vertex):
        """Removes vertex and all incident edges from self.

        Called by the /= operator.
        """

        self.remove_vertex(vertex)

    def __isub__(self, edge):
        """Removes edge from self, leaving the endpoints in self.

        Called by the -= operator.
        """

        self.remove_edge(edge)

    def __iter__(self):
        """Returns an iterator over the vertices of self.

        The implementation provided here does not guarantee any order to the
            vertices seen while iterating.
        """

        # TODO (challenge): Modify __iter__ so that it performs either a depth-
        #     first or breadth-first search of self.vertices.
        # Hint: use one of the generator functions below to do this.
        return iter(self.vertices)

    def depth_first_search(self, start=None):
        """Generator function to perform breadth-first search on self.vertices.

        If start is not specified, then no particular vertex is guaranteed to
            be the first one selected, and all subsequent calls to __next__
            will return one of the vertices adjacent to the previous one, in an
            order consistent with the classical BFS algorithm.

        Note: if self is an unconnected graph, breadth_first_search WILL NOT
            visit all vertices!
        """

        # TODO (challenge): Implement this generator function
        # Hint: make calls to the abstract methods above, making no assumptions
        #     about the representation of self.
        # Hint: the yield from statement helps yield values propagate up the
        #     call stack, allowing for recursive generator functions.
        raise NotImplementedError

    def breadth_first_search(self, start=None):
        """Generator function to perform breadth-first search on self.vertices.

        If start is not specified, then no particular vertex is guaranteed to
            be the first one selected, and all subsequent calls to __next__
            will return one of the vertices adjacent to the previous one, in an
            order consistent with the classical BFS algorithm.

        Note: if self is an unconnected graph, breadth_first_search WILL NOT
            visit all vertices!
        """

        # TODO (challenge): Implement this generator function
        # Hint: make calls to the abstract methods above, making no assumptions
        #     about the representation of self.
        raise NotImplementedError

class EdgelistGraph(Graph):
    """An edge list representation of a Graph.

    A ListGraph has one private instance variable, _edgelist.
    """

    def __init__(self, edgelist=None):
        """Returns an EdgelistGraph generated from edgelist."""

        self._edgelist = edgelist or []

    def __repr__(self):
        return repr(self._edgelist)

    @property
    def vertices(self) -> set:
        # TODO: Implement this method
        raise NotImplementedError

    @property
    def edges(self) -> set:
        # TODO: Implement this method
        raise NotImplementedError

    def degree(self, vertex) -> int:
        # TODO: Implement this method
        raise NotImplementedError

    def adjacent_to(self, vertex) -> set:
        # TODO: Implement this method
        raise NotImplementedError

    def add_vertex(self, vertex):
        # TODO: Implement this method
        raise NotImplementedError

    def add_edge(self, edge):
        # TODO: Implement this method
        raise NotImplementedError

    def remove_vertex(self, vertex):
        # TODO: Implement this method
        raise NotImplementedError

    def remove_edge(self, edge):
        # TODO: Implement this method
        raise NotImplementedError

class MatrixGraph(Graph):
    """An adjacency-matrix representation of a Graph.

    A MatrixGraph has one private instance variable, _matrix.
    """

    # TODO (challenge): accept and keep track of arbitrary vertex indices.

    def __init__(self, matrix=None):
        """Produces a MatrixGraph generated from matrix."""

        self._matrix = matrix or []

    def __repr__(self):
        return repr(self._matrix)

    @property
    def vertices(self) -> set:
        # TODO: Implement this method
      output=set()
      for i in range(len(self._matrix)):
        output.add(i)
      return output
      

    @property
    def edges(self) -> set:
      # TODO: Implement this method
      output=set()
      for i in range(len(self._matrix[0])):
        for j in range(len(self._matrix[0])):
          if(self._matrix[i-1][j-1])==True:
            output.add((i,j))        
      return output
    def degree(self, vertex) -> int:
        # TODO: Implement this method
      output=0;
      for i in range(len(self._matrix)):
        if(self._matrix[i][vertex]==True):
          output=output+1
      return output
    def adjacent_to(self, vertex) -> set:
        # TODO: Implement this method
      output=set()
      for i in range(len(self._matrix[0])):
        if(self._matrix[i][vertex]==True):
          output.add(i)
      return output
    def add_vertex(self, vertex):
      holder=[]
      for i in range(len(self._matrix)):
        self._matrix[i].append(False)
        holder.append(False)
      holder.append(False)
      self._matrix.append(holder)
      
          

    def add_edge(self, edge):
        # TODO: Implement this method
        self._matrix[edge[0]-1][edge[1]-1]=True
        self._matrix[edge[1]-1][edge[0]-1]=True
    def remove_vertex(self, vertex):
        # TODO: Implement this method
      for i in range(len(self._matrix[0])):
        del self._matrix[i][vertex]
      self._matrix.pop(vertex)
      
          

    def remove_edge(self, edge):
        # TODO: Implement this method
        self._matrix[edge[0]-1][edge[1]-1]=False
        self._matrix[edge[1]-1][edge[0]-1]=False

class DictGraph(Graph):
    """An adjacency-list representation of a Graph.

    A DictGraph has one private instance variable, _dict.
    """

    def __init__(self, dictionary=None):
        """Produces a DictGraph generated from dictionary."""

        self._dict = dictionary or {}

    def __repr__(self):
        return repr(self._dict)

    @property
    def vertices(self) -> set:
        # TODO: Implement this method
        raise NotImplementedError

    @property
    def edges(self) -> set:
        # TODO: Implement this method
        raise NotImplementedError

    def degree(self, vertex) -> int:
        # TODO: Implement this method
        raise NotImplementedError

    def adjacent_to(self, vertex) -> set:
        # TODO: Implement this method
        raise NotImplementedError

    def add_vertex(self, vertex):
        # TODO: Implement this method
        raise NotImplementedError

    def add_edge(self, edge):
        # TODO: Implement this method
        raise NotImplementedError

    def remove_vertex(self, vertex):
        # TODO: Implement this method
        raise NotImplementedError

    def remove_edge(self, edge):
        # TODO: Implement this method
        raise NotImplementedError
