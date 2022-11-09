import heapq
class Solution:
    def solve(self, A, B):
        H = []
        heapq.heapify(H)
        n = len(A)
        B =((n*(n-1))/2)-B+1 # for minheap
        
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                heapq.heappush(H,(A[i]/A[j],[A[i],A[j]]))
                if len(H)>B:
                    heapq.heappop(H)
        _,ans = heapq.heappop(H)
        return ans
