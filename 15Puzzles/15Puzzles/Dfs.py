import numpy as np
from Node import Node
from queue import LifoQueue

class Dfs(object):
    """description of class"""
    def __init__(self, startNode, endNode):
        self.__start = startNode
        self.__end = endNode
        self.__visited = []
        self.solutionNode = None
        self.__queue = LifoQueue()

    def dfs_iterative(self):

        self.__queue.put(self.__start)
        while not self.__queue.empty():            
            lastNode = self.__queue.get()
            self.__visited.append(lastNode)
            if lastNode == self.__end: 
                self.solutionNode = lastNode
                break

            children = lastNode.getChildren()
            for move, puzzles in sorted(children.items(), reverse=True):
                newNode = Node(puzzles, lastNode, move)
                if newNode in self.__visited: continue
                ''' 
                to co wrzucimy w petli ostatnie bedzie brane jako pierwsze, 
                dlatego odwracam liste
                '''
                self.__queue.put(newNode)

    def dfs_recursive(self, node):

        self.__visited.append(node)
        print(node)
        if node == self.__end:
            self.solutionNode = node
            return 0

        children = node.getChildren()
        
        for move, puzzles in children.items():
            newNode = Node(puzzles, node, move)
            
            if newNode in self.__visited: continue

            self.dfs_recursive(newNode)
            '''
            zatrzymuje DFSa jak znajde noda koncowego,
            bo po co ma mi przeszukiwać dalej skoro znalazl
            '''
            if self.solutionNode: break

    def solve(self):
        #self.dfs_recursive(self.__start)
        self.dfs_iterative()


