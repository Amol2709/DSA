class Solution:
    def generateMatrix(self, A):
        ans = [[0 for i in range(A)] for j in range(A)]
        T=0
        L=0
        R=A-1
        B=A-1
        count = 0
        while(count<A**2):
            for k in range(L,R+1):
                ans[T][k]=count+1
                count = count+1
            T=T+1
            for k in range(T,B+1):
                ans[k][R]=count+1
                count=count+1
            R=R-1
            for k in range(R,L-1,-1):
                ans[B][k]=count+1
                count=count+1
            B=B-1
            for k in range(B,T-1,-1):
                ans[k][L]=count+1
                count=count+1
            L=L+1
        return ans

