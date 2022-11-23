# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, targetSum: int) -> int:
        self.count = 0
        self.target = targetSum
        self.func(root,[])
        return self.count
    def func(self,node,arr):
        if node == None:
            return
        tmp_arr =[node.val]+arr
        curr_val = 0
        for elem in tmp_arr:
            curr_val+=elem
            if curr_val == self.target:
                self.count+=1
        self.func(node.left,tmp_arr)
        self.func(node.right,tmp_arr)
