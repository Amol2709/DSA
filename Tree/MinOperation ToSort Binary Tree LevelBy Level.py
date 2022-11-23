# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root) -> int:
        def MinSwapToMakeArraySort(arr):
            '''

            [7,6,5,8]

            original = [(7,0),(6,1),(5,2),(8,3)]
            sorted = [(5,2),(6,1),(7,0),(8,3)]
            '''
            swap = 0
            tmp_arr = []
            for i in range(len(arr)):
                tmp_arr.append((arr[i],i))
            tmp_arr.sort()

            for i in range(0,len(arr)):
                value,index = tmp_arr[i][0],tmp_arr[i][1]
                while(i!=index):
                    value_at_index = tmp_arr[index]

                    new_index = value_at_index[1]

                    tmp_arr[index],tmp_arr[new_index] = tmp_arr[new_index],tmp_arr[index]

                    index = tmp_arr[i][1]
                    
                    swap+=1
            return swap
        
        from collections import deque
        Q = deque()
        
        Q.append(root)
        Q.append(None)
        level_order = []
        tmp = []
        
        while(True):
            node = Q.popleft()
            if node == None:
                level_order.append(tmp)
                tmp = []
                if len(Q)==0:
                    break
                else:
                    Q.append(None)
            else:
                tmp.append(node.val)
                if node.left !=None:
                    Q.append(node.left)
                if node.right!=None:
                    Q.append(node.right)
        ans = 0
        #print(level_order)
        for i in range(len(level_order)):
            ans+=MinSwapToMakeArraySort(level_order[i])
        return ans
                    