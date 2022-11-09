# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    def postorderTraversal(self, A):
        stk = []
        ans = []
        curr = A 

        while(len(stk)!=0 or curr != None):
            if curr == None:
                curr = stk.pop().left
            else:
                ans.append(curr.val)
                stk.append(curr)
                curr = curr.right
        ans.reverse()
        return ans
            
