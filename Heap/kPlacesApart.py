class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B): 
        import heapq
        min_heap=[]
        heapq.heapify(min_heap)
        Ans = []
        N  = len(A)
        for i in range(N):
            heapq.heappush(min_heap,A[i])
            if len(min_heap)>B:
                Ans.append(heapq.heappop(min_heap))

        while(len(min_heap)>0):
            Ans.append(heapq.heappop(min_heap))
        return Ans


            