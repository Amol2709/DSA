class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        if len(A)==2:
            return sum(A)
        if len(A)==1:
            return A[0]
        import heapq
        N=len(A)
        heapq.heapify(A)
        cost=0
        while(len(A)>=2):
            rope1=heapq.heappop(A)
            rope2=heapq.heappop(A)
            cost= cost+rope1+rope2
            heapq.heappush(A,rope1+rope2)
        return cost
