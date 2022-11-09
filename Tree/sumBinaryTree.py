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
        flag,_=self.func(A)
        if flag:
            return 1
        return 0
    def func(self,node):
        if node == None:
            return True,0
        if node.left == node.right == None:
            return True, node.val
        left,left_sum =self.func(node.left)
        right,right_sum =self.func(node.right)

        if left and right:
            if node.val == left_sum+right_sum:
                return True,node.val+left_sum+right_sum
            else:
                return False,-1
        else:
            return False,-1
            

