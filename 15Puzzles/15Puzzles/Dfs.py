import numpy as np
from Node import Node

class Dfs(object):
    """description of class"""
    def __init__(self, startNode, endNode):
        self.__start = startNode
        self.__end = endNode
        self.__visited = []
        self.visitedNodeCounter = 0
        self.solutionNode = None

    def dfs(self, node):

        self.__visited.append(node)
        self.visitedNodeCounter += 1

        if node == self.__end:
            self.solutionNode = node
            return

        children = node.getChildren()
        for move, puzzles in children.items():
            newNode = Node(puzzles, node, move)
            if newNode in self.__visited: continue
            self.dfs(newNode)

    def solve(self):
        self.dfs(self.__start)


