# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        self.count = 0
        self.sum = targetSum
        def runDFS(node, arr):
            if not node:
                return arr
            
            tmp = []
            for num in arr:
                tmp.append(num+node.val)
            arr = tmp+[node.val]
            

            for num in arr:
                if num == self.sum:
                    self.count += 1

            runDFS(node.left, arr)
            runDFS(node.right, arr)

        runDFS(root, [])
        return self.count
        