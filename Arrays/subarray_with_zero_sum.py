# Exist or Not

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        p=[]
        temp=0
        for i in range(0,len(A)):
            if A[i]==0:
                return 1
            temp = temp+A[i]
            p.append(temp)
        S=set()
        for i in p:
            if i in S:
                return 1
            elif i==0:
                return 1
            else:
                S.add(i)
        return 0

            
