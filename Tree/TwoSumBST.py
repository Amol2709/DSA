# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    def t2Sum(self, A, B):
        self.traverse = []
        self.B= B
        self.func(A)
        if self.TwoPtr():
            return 1
        else:
            return 0
    def TwoPtr(self):
        ptr1,ptr2 = 0,len(self.traverse)-1
        while(ptr1<ptr2):
            if self.traverse[ptr1]+self.traverse[ptr2]==self.B:
                return True
            if self.traverse[ptr1]+self.traverse[ptr2]>self.B:
                ptr2 = ptr2-1
            else:
                ptr1 = ptr1+1
        return False
    def func(self,node):
        if node == None:
            return 
        self.func(node.left)
        self.traverse.append(node.val)
        self.func(node.right)
