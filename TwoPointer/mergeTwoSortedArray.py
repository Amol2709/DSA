class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def solve(self, A, B):
        ans = []
        ptr1,ptr2 = 0,0
        
        while(ptr1<len(A) and ptr2<len(B)):
            if A[ptr1]<B[ptr2]:
                ans.append(A[ptr1])
                ptr1+=1
            else:
                ans.append(B[ptr2])
                ptr2+=1
        if ptr1<len(A):
            ans = ans+list(A[ptr1:])
        if ptr2<len(B):
            ans = ans + list(B[ptr2:])
        return ans
