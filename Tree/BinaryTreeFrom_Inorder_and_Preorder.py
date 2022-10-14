# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


# @param A : list of integers
	# @param B : list of integers
	# @return the root node in the tree
    # inorder = left root right 
    # preorder = root left right
    # right left root
class Solution:
    def buildTree(self, A, B):
        self.A = A
        self.map = {}
        self.B = B
        for i in range(len(B)):
            self.map[B[i]]=i
        self.A.reverse()

        low,high = 0,len(B)-1
        return self.myFunc(low,high)
    def myFunc(self,low,high):
        if low>high:
            return None
        elem = self.A.pop()
        node = TreeNode(elem)
        mid = self.map[elem]
        node.left = self.myFunc(low,mid-1)
        node.right = self.myFunc(mid+1,high)
        return node



