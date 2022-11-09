from collections import deque
class Solution:
    # @param A : integer
    # @return a strings
    def solve(self, A):
        q = deque()
        q.append(1)
        q.append(2)

        # ans = []
        while A > 0:
            cur_ele = q.popleft()
            # ans.append( int( str(cur_ele) + str(cur_ele)[::-1] ) )

            for i in range(1,3):
                value = ( cur_ele * 10 )+ i
                q.append(value)
            A -= 1


        return int( str(cur_ele) + str(cur_ele)[::-1] )
