'''
class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''

#Function to convert a binary tree to doubly linked list.
class Solution:
    def bToDLL(self,root):
        # do Code here
        self.prev = None
        self.func(root)
        return self.head
    def func(self,node):
        if node == None:
            return 
        
        self.func(node.left)
        if self.prev == None:
            self.head = node
        else:
            node.left = self.prev
            self.prev.right = node
        
        
        self.prev = node
        self.func(node.right)

