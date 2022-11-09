
'''
Given N bags, each bag contains Bi chocolates. There is a kid and a magician.
In a unit of time, the kid can choose any bag i, and eat Bi chocolates from it,
 then the magician will fill the ith bag with floor(Bi/2) chocolates.

Find the maximum number of chocolates that the kid can eat in A units of time.

NOTE:

floor() function returns the largest integer less than or equal to a given number.
Return your answer modulo 109+7


'''


class Solution:
    def nchoc(self, A, B):
        import heapq
        H=[]
        heapq.heapify(H)
        N=len(B)
        for i in range(N):
            heapq.heappush(H,-1*B[i])
        ans = 0
        for i in range(A):
            x= heapq.heappop(H)
            ans = ans+(-1*x)
            x= int(x/2)
            heapq.heappush(H,x)
        return int(ans % (1e9 + 7))
            

