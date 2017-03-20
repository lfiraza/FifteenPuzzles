import numpy as np

class Bfs(object):
    """description of class"""

    def __init__(self, startNode, endNode):
        self.__start = startNode
        self.__end = endNode
        self.visited = []
        self.visitedNodeCounter = 0

