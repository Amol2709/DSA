class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @param D : list of integers
    # @param E : list of integers
    # @return a list of integers
    def solve(self, A, B, C, D, E):
        import numpy as np 
        prefix = np.zeros((len(A),len(A[0])))
        temp=0
        for i in range(0,len(A[0])):
            temp = temp + A[0][i]
            prefix[0][i] = int(temp)
        temp=0
        for i in range(0,len(A)):
            temp = temp + A[i][0]
            prefix[i][0] = int(temp)
        for i in range(1,len(A)):
            for j in range(1,len(A[0])):
                prefix[i][j]=int(prefix[i][j-1]+prefix[i-1,j]-prefix[i-1,j-1]+A[i][j])
        Ans=[]
        for i in range(0,len(B)):
            r1 = B[i]-1
            c1 = C[i]-1
            r2 = D[i]-1
            c2 = E[i]-1
            res = prefix[r2][c2]
            if r1>0:
                res = res-prefix[r1-1][c2]
            if c1>0:
                res = res-prefix[r2][c1-1]
            if r1>0 and c1>0:
                res = res+ prefix[r1-1][c1-1]
            # if r1 ==0 and c1!=0:
            #     s = prefix[r2][c2]-prefix[r2][c1-1]
            # elif c1==0 and r1!=0:
            #     s= prefix[r2][c2]-prefix[r1-1][c2]
            # elif c1==0 and r1==0:
            #     s  = prefix[r2][c2]
            # else:
            #     s= prefix[r2][c2]-prefix[r2][c1-1]-prefix[r1-1][c2]+prefix[r1-1][c1-1]
            Ans.append(int(res)% int(1e9+7))
        return Ans

