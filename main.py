from point import Point
from queue import Queue
from cluster import Cluster
from counter import MeowCounter
import sys
def find_n(point, eps, point_list):
    n = []
    for p in point_list:
        if Point.distance(point, p) < eps:
            n.append(p)
    return n

def dbscan(eps, minpts, point_list):
    counter = MeowCounter()
    cluster_list = []
    for p in point_list:
        if p.label is None:
            p.label = "visited"
            counter.count()
            n_eps = find_n(p, eps, point_list)
            if len(n_eps) < minpts:
                p.label = "noise"
            else:
                cluster = Cluster()
                cluster_list.append(cluster)
                cluster.add_point(p)
                while len(n_eps) > 0:
                    p_p = n_eps.pop()
                    if p_p.label is None:
                        p_p.label = "visited"
                        counter.count()
                        n_eps_2 = find_n(p_p, eps, point_list)
                        if len(n_eps_2) >= minpts:
                            for i in n_eps_2:
                                if i.label is None:
                                    n_eps.append(i)

                    if p_p.cluster is None:
                        cluster.add_point(p_p)
    return cluster_list

if __name__ == "__main__":
    # filename = sys.argv[1]
    filename = "test_input.txt"
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    point_list = []
    for line in lines:
        data = line.split(" ")
        point = Point(int(data[0]), (float(data[1]), float(data[2])))
        point_list.append(point)

    cluster_list = dbscan(eps=4, minpts=6, point_list=point_list)

    c = 1
    for cluster in cluster_list:
        id_str = []
        for point in cluster.points:
            id_str.append(str(point.id))
        id_str = " ".join(id_str)
        print(str(c)+": " + id_str)
        c+=1