class Cluster:
    def __init__(self):
        self.points = []

    def add_point(self, p):
        self.points.append(p)
        p.cluster = self