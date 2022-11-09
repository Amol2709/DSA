class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        ans = []
        ans.append(A[0])
        ptr1 = 1
        while(ptr1<len(A)):
            if ans[-1]==A[ptr1]:
                ptr1+=1
            else:
                ans.append(A[ptr1])
                ptr1+=1
        return ans
