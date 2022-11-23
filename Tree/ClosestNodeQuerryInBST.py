# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        self.inorder = []
        self.InorderTraversal(root)
        self.n = len(self.inorder)
        ans  = []
        for i in range(len(queries)):
            ans.append(self.applyBinarySearch(queries[i]))
        return ans
    
    def applyBinarySearch(self,val):
        low,high = 0,self.n-1
        tmp =-1
        ans_high=ans_low=-1
        while(low<=high):
            mid = (low+high)//2
            
            if self.inorder[mid]==val:
                return [val,val]
            
            elif self.inorder[mid]>val:
                high = mid-1
                ans_high = self.inorder[mid]
            else:
                low = mid+1
                ans_low = self.inorder[mid]
                
        return [ans_low,ans_high]
    
    # def applyBinarySearchMin(self,val):
    #     low,high = 0,self.n-1
    #     tmp =-1
    #     while(low<=high):
    #         mid = (low+high)//2
            
    #         if self.inorder[mid]==val:
    #             return val
            
    #         elif self.inorder[mid]>val:
    #             high = mid-1
    #         else:
    #             low = mid+1
    #             tmp = self.inorder[mid]
    #     return tmp
            
        
        
        
        
        
    def InorderTraversal(self,node):
        if node == None:
            return
        self.InorderTraversal(node.left)
        self.inorder.append(node.val)
        self.InorderTraversal(node.right)
    

            
            
        
        
        
        
       
        