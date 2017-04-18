import numpy as np
from Node import Node
from queue import LifoQueue

class Dfs(object):
    """description of class"""
    def __init__(self, startNode, endNode, settings):
        self.__start = startNode
        self.__end = endNode
        self.__visited = {}
        self.solutionNode = None
        self.__queue = LifoQueue()
        self.__settings = settings

    def dfs_iterative(self):

        moves = np.array(['G', 'D', 'L', 'P'])

        if(self.__settings[0]!='R'):
            moves = self.__settings

        self.__queue.put(self.__start)
        while not self.__queue.empty():            
            lastNode = self.__queue.get()
            self.__visited[lastNode.hash] = None
            if lastNode == self.__end: 
                self.solutionNode = lastNode
                break

            children = lastNode.getChildren()
            if(self.__settings[0]=='R'):
                np.random.shuffle(moves)

            for move in sorted(moves, reverse=True):
                if move in children:
                    newNode = Node(children[move], lastNode, move)
                    if newNode.hash in self.__visited: continue
                    ''' 
                    to co wrzucimy w petli ostatnie bedzie brane jako pierwsze
                    '''
                    self.__queue.put(newNode)

    def dfs_recursive(self, node):

        moves = np.array(['G', 'D', 'L', 'P'])

        if(self.__settings[0]!='R'):
            moves = self.__settings

        self.__visited[node.hash] = None
        print(node)
        if node == self.__end:
            self.solutionNode = node
            return

        children = node.getChildren()
        if(self.__settings[0]=='R'):
                np.random.shuffle(moves)

        for move in moves:
            if move in children:
                newNode = Node(children[move], node, move)
                if newNode.hash in self.__visited: continue
                self.dfs_recursive(newNode)
                '''
                zatrzymuje DFSa jak znajde noda koncowego,
                bo po co ma mi przeszukiwać dalej skoro znalazl
                '''
                if self.solutionNode: break

    def solve(self):
        #self.dfs_recursive(self.__start)
        self.dfs_iterative()


