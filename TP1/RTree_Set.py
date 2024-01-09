# -*- coding: utf-8 -*-
"""
RTree module to build and manage rooted tree
"""
class Rtree:
    """
    A rooted tree is represented by
    A set of vertices
    A set of edges
    """
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        # Test
        V = [0, 1, 2, 3, 4, 5, 6]
        E = [(0,1), (0,2), (0,3), (1,4), (1,5), (1,6)]


    def root(self):
	"""
	Return the root of rooted tree
	root : Rtree → Node
	"""
	# Extract all father nodes and remove double
	f = set([e[0] for e in self.E])
	# Extract all children nodes and remove double
	c = set([e[1] for e in self.E])
	# remove children nodes from father list: compute r = f - c 
	r = [e for e in f if e not in c]
	return r[0]
    
rt = Rtree(V, E)
