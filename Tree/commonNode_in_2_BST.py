# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
class Traverse:
    def Main(self,root):
        self.node = root
        self.s = set()
        self.traverse(root)
        return self.s
    def traverse(self,root):
            if root == None:
                return 
            self.s.add(root.val)
            self.traverse(root.left)
            self.traverse(root.right)
class Solution:
    def solve(self, A, B):
        obj1=  Traverse()
        s1 = obj1.Main(A)
        
        obj2 =  Traverse()
        s2 = obj1.Main(B)
        
        if len(s1.intersection(s2))==0:
            return 0
        else:
            return int(sum(s1.intersection(s2)) % (1e9+7))

