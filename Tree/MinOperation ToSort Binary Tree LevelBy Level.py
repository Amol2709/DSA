# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def check(arr):
            n = len(arr)
            arrpos = [*enumerate(arr)]


            arrpos.sort(key = lambda it : it[1])


            vis = {k : False for k in range(n)}


            ans = 0
            for i in range(n):

                # already swapped or
                # already present at
                # correct position
                if vis[i] or arrpos[i][0] == i:
                    continue

                # find number of nodes
                # in this cycle and
                # add it to ans
                cycle_size = 0
                j = i

                while not vis[j]:

                    # mark node as visited
                    vis[j] = True

                    # move to next node
                    j = arrpos[j][0]
                    cycle_size += 1

                # update answer by adding
                # current cycle
                if cycle_size > 0:
                    ans += (cycle_size - 1)

            # return answer
            return ans
        
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
            ans+=check(level_order[i])
        return ans
                    