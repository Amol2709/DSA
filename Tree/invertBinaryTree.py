# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    def invertTree(self, A):
        return self.myFunc(A)
    def myFunc(self, node):
        if node == None:
            return None 
        rightNode = node.right 
        node.right = self.myFunc(node.left)
        node.left = self.myFunc(rightNode)
        return node
