
'''
Given a binary search tree.
Return the distance between two nodes with given two keys B and C. It may be assumed that both keys exist in BST.

NOTE: Distance between two nodes is number of edges between them.

'''

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
import sys
class Solution:
    def solve(self, A, B, C):
        self.B = min(B,C)
        self.C = max(B,C)
        lca = self.FindLCA(A)
        self.target = self.B
        distance_left = self.findDistance(lca)
        self.target = self.C
        distance_right = self.findDistance(lca)
        return distance_left+distance_right
    def findDistance(self,node):
        if node == None:
            return sys.maxsize
        if node.val == self.target:
            return 0
        return 1+min(self.findDistance(node.left),self.findDistance(node.right))


    def FindLCA(self,node):
        if node == None:
            return None
        if self.B<=node.val<=self.C:
            return node
        elif node.val>self.C:
            return self.FindLCA(node.left)
        else:
            return self.FindLCA(node.right)



