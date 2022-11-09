class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextGreater(self, A):
        stk = [A[-1]]
        nge = [-1]*len(A)
        for i in range(len(A)-2,-1,-1):
            if A[i]>=stk[-1]:
                while(True):
                    if len(stk)==0:
                        stk.append(A[i])
                        break
                    if A[i]>=stk[-1]:
                        stk.pop()
                    else:
                        nge[i] = stk[-1]
                        stk.append(A[i])
                        break
            else:
                nge[i] = stk[-1]
                stk.append(A[i])
        return nge

