from collections import deque
class Solution:
    # @param A : integer
    # @return a list of integers
    def solve(self, A):
        if A<=3:
            return list(range(1,A+1))
        ans = [1,2,3]
        Q=deque()
        Q.append(1)
        Q.append(2)
        Q.append(3)
        

        while(len(Q)!=0):
            num = Q.popleft()
            for i in range(1,4):
                elem = int(str(num)+str(i))
                Q.append(elem)
                ans.append(elem)
                if len(ans)==A:
                    return ans
            

