'''
Given 2 integers A and B and an array of integers C of size N. Element C[i]
 represents the length of ith board.
You have to paint all N boards [C0, C1, C2, C3 … CN-1]. 
There are A painters available and each of them takes 
B units of time to paint 1 unit of the board.

Calculate and return the minimum time required to paint 
all boards under the constraints that any painter will only
 paint contiguous sections of the board.
NOTE:
1. 2 painters cannot share a board to paint. 
    That is to say, a board cannot be painted partially by one painter, and partially by another.
2. A painter will only paint contiguous boards. 
    This means a configuration where painter 1 paints boards 1 and 3 but not 2 is invalid.
'''

class Solution:
    def paint(self, A, B, C):
        low, high = max(C)*B, sum(C)*B

        def isPossible(time):
            painter = 1
            currTime = C[0]*B
            for i in range(1,len(C)):
                tempTime = C[i]*B
                if currTime+tempTime>time:
                    painter = painter+1
                    currTime = tempTime
                else:
                    currTime = currTime+tempTime
                
            
            if painter<=A:
                return True
            return False

        while(low<=high):
            mid = (low+high)//2
            if isPossible(mid):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return int(ans%(1e7+3))

