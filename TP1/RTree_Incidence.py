# -*- coding: utf-8 -*-
import numpy as np
"""
RTree module to build and manage rooted tree
"""
class Rtree:
    """
    A rooted tree is represented by an incidence matrix
    """
    def __init__(self, incidence):
        self.incidence = incidence

    def root(self):
        """
        Return the root of rooted tree
        root : Rtree -> Node

        Author: Damien Djomby
        """

        # Translate all negative or null values of incidence matrix to True
        # and False otherwise
        incidenceAsBool = np.asarray(self.incidence <= 0)
        
        # For all nodes we check along the line axis if all values
        # are True
        isNodesRoot = np.all(incidenceAsBool, axis=1)
        
        # Now we'll get the id of the only root node which means:
        # - We subscript to get the first element (the only one actually)
        # - We subscript a second time to get the first coordonate of the
        #   element (which is also the only one)
        return np.argwhere(isNodesRoot)[0][0]
    
incidence = np.matrix([
  [-1, -1, -1, 0,  0,  0],
  [1,  0,  0, -1, -1, -1], 
  [0,  1,  0,  0,  0,  0 ], 
  [0,  0,  1,  0,  0,  0 ], 
  [0,  0,  0,  1,  0,  0 ], 
  [0,  0,  0,  0,  1,  0 ], 
  [0,  0,  0,  0,  0,  1 ]])

rt = Rtree(incidence)

print(rt.root())

