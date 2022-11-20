# Definition for a binary tree node.

### Leetcode: 2476
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        self.inorder = []
        self.InorderTraversal(root)
        self.n = len(self.inorder)
        ans  = []
        for i in range(len(queries)):
            ans.append([self.applyBinarySearchMin(queries[i]),self.applyBinarySearchMax(queries[i])])
        return ans
    
    def applyBinarySearchMax(self,val):
        low,high = 0,self.n-1
        tmp =-1
        while(low<=high):
            mid = (low+high)//2
            
            if self.inorder[mid]==val:
                return val
            
            elif self.inorder[mid]>val:
                high = mid-1
                tmp = self.inorder[mid]
            else:
                low = mid+1
                
        return tmp
    
    def applyBinarySearchMin(self,val):
        low,high = 0,self.n-1
        tmp =-1
        while(low<=high):
            mid = (low+high)//2
            
            if self.inorder[mid]==val:
                return val
            
            elif self.inorder[mid]>val:
                high = mid-1
            else:
                low = mid+1
                tmp = self.inorder[mid]
        return tmp
            
        
        
        
        
        
    def InorderTraversal(self,node):
        if node == None:
            return
        self.InorderTraversal(node.left)
        self.inorder.append(node.val)
        self.InorderTraversal(node.right)
    

            
            
        
        
        
        
       
        