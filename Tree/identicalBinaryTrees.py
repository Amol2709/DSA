# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    def isSameTree(self, A, B):
        if self.myFunc(A,B):
            return 1
        return 0
    def myFunc(self,node1, node2):
        if node1 == None and node2 == None:
            return True
        if (node1 == None and node2!=None) or (node2 ==None and node1!=None):
            return False
        if node1.val == node2.val:
            return self.myFunc(node1.left, node2.left) and self.myFunc(node1.right, node2.right)
        else:
            return False
