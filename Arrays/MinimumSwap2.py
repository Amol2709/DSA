class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        count = 0
        for i in range(len(A)):
            while(A[i]!=i):
                index = i
                value = A[i]
                A[index] = A[A[index]]
                A[value] = value
                count = count+1
        return count

