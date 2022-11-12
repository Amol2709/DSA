from collections import deque
class Solution:
    # @param A : integer
    # @return a list of integers
    # 1 2 3 11 12 13 21 22 23 111 112 113 121 122 123
    def solve(self, A):
        if A<=3:
            return list(range(1,A+1))
        ans = [1,2,3]
        Q=deque()
        Q.append(1)
        Q.append(2)
        Q.append(3)
        

        for i in range(4,A+1):
            num = Q.popleft()
            for i in range(1,4):
                elem = (num*10)+i
                ans.append(elem)
                Q.append(elem)
                if len(ans)==A:
                    return ans
        return ans
