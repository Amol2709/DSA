# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        self.map_={}
        return self.func(node)
    def func(self,node):
        if node == None:
            return node

        if node.label in self.map_:
            return self.map_[node.label]
        newNode = UndirectedGraphNode(node.label)
        self.map_[node.label] = newNode
        for _ in node.neighbors:
            newNode.neighbors.append(self.func(_))
        return newNode
        
