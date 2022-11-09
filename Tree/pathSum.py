# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    def hasPathSum(self, A, B):
        self.ans = False
        self.target = B 
        self.func(A,0)
        if self.ans:
            return 1
        return 0
    def func(self,node,curr_sum):
        if node == None:
            return 
        if node.left == None and node.right == None:
            if curr_sum+node.val == self.target:
                self.ans  = True
            return 
        self.func(node.left,curr_sum+node.val)
        self.func(node.right,curr_sum+node.val)

