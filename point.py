import numpy as np
class Point:
    def __init__(self, id, coord):
        self.coord = np.array(coord)
        self.id = id
        self.n_neighbor = 0
        self.label = None
        self.cluster = None

    @staticmethod
    def distance(a, b):
        return np.linalg.norm(a.coord - b.coord)
