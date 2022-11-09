
'''
Given an integer array B of size N.

You need to find the Ath largest element in the subarray [1 to i], where i varies from 1 to N. In other words, find the Ath largest element in the sub-arrays [1 : 1], [1 : 2], [1 : 3], ...., [1 : N].

NOTE: If any subarray [1 : i] has less than A elements, then the output should be -1 at the ith index.
A = 4  
 B = [1 2 3 4 5 6] 
Ans = [-1, -1, -1, 1, 2, 3]

A = 2
 B = [15, 20, 99, 1]
 Ans = [-1, 15, 20, 20]
'''

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        import heapq
        H=[]
        heapq.heapify(H)
        N=len(B)
        Ans = []
        for i in range(N):
            if i+1<=A:
                heapq.heappush(H,B[i])
                continue
    
            Ans.append(H[0])
            if B[i]>H[0]:
                heapq.heappop(H)
                heapq.heappush(H,B[i])
        Ans.append(H[0])
        return [-1]*(A-1)+Ans
