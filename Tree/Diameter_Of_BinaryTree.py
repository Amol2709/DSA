# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        self.ans=0
        self.func(A)
        return self.ans
    def func(self,node):
        if node == None:
            return 0
        if node.left == node.right == None:
            return 1
        
        left_height  = self.func(node.left)
        right_height = self.func(node.right)

        self.ans = max(self.ans,left_height+right_height)
        return 1+max(left_height,right_height)
        


