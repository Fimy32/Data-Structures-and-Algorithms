import sys
import heapq
from heapq import heappush, heappop


class Node:
    def __init__(self, name,):
        self.name = name
        self.parent = None
        edges = []
        self.startdistance = sys.maxsize
        self.isopenlist = False
        removed = False

    def add_edge(self, edge):
        self.edges.append(edge)


class Edge:
    def __init__(self, start, end, distance):
        self.start = start
        self.end = end
        self.distance = distance


class Grapth:
    def __init__(self):
        self.nodes = []


    def addNode(self, node):
        self.nodes.append(node)

    def addEdge(self, start, end, distance):
        start.add_edge(Edge(start, end, distance))
        end.add_edge(Edge(end, start, distance))

    def dijkstra(self, start, end):
        self.currentnode = start
        self.openlist = Priority_Queue()




class Priority_Queue:
    def __init__(self):
        self.heaps = []

    def push(self, value):
        heappush(self.heaps, value)

    def pop(self):
        heappop(self.heaps)


