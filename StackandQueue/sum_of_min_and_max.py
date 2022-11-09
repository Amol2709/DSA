import sys
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        from collections import deque
        if B==1:
            return 2*sum(A)
        if B==len(A):
            return min(A)+max(A)
        
        Q = deque()
        N = len(A)
        temp = -sys.maxsize
        for i in range(0,B):
            if A[i]>temp:
                temp=A[i]
                index = i

        Q.append((temp,index))
        Ans = []
        for i in range(0,N):
            temp = Q[0][0]
            index = Q[0][1]
            if index>=i:
                pass
            else:
                while(True):
                    if len(Q)==0:
                        Q.append((A[i],i))
                        break
                    if A[i]<Q[-1][0]:
                        Q.append((A[i],i))
                        break
                    else:
                        Q.pop()
            if i>=B-1:
                while(True):
                    if i-Q[0][1]<=B-1:
                        break
                    else:
                        Q.popleft()
                        
                Ans.append(Q[0][0])
        # from collections import deque
        # if B==1:
        #     return A
        Q = deque()
        N = len(A)
        temp = sys.maxsize
        for i in range(0,B):
            if A[i]<temp:
                temp=A[i]
                index = i

        Q.append((temp,index))
        Ans1 = []
        for i in range(0,N):
            temp = Q[0][0]
            index = Q[0][1]
            if index>=i:
                pass
            else:
                while(True):
                    if len(Q)==0:
                        Q.append((A[i],i))
                        break
                    if A[i]>Q[-1][0]:
                        Q.append((A[i],i))
                        break
                    else:
                        Q.pop()
            if i>=B-1:
                while(True):
                    if i-Q[0][1]<=B-1:
                        break
                    else:
                        Q.popleft()
                        
                Ans1.append(Q[0][0])
        s = 0
        for i in range(len(Ans)):
            s = s+Ans[i]+Ans1[i]
        return int(s % (1e9+7))

            
            
