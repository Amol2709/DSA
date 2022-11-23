class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        n = len(A)
        _min = 0
        _max =0
        for i in range(0,n):
            temp = A[i]*(2**(n-1-i))
            _min+=temp
        for j in range(n-1,-1,-1):
            temp = A[j]*(2**(j))
            _max+=temp
        return int(_max-_min)%int(1e9+7)

    