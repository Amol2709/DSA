class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        Ans = []
        n = len(A)
        for i in range(len(B)):
            rot = B[i]%n
            Ans.append(A[rot:]+A[:rot])
        return Ans
