class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        ans = 0
        n= len(A)
        for i in range(0,32):
            ind=n
            for j in range(n-1,-1,-1):
                bit = bool((A[j] >> i) &1)
                if bit:
                    ind = j
                ans = ans + (n-ind)*pow(2,i) 
                # ans = ans + (N-j)*(2**ind)
                # if (A[j]>>i) & 1 ==1:
                #     ans = ans + (N-j)*(2**i)*factor
                #     factor=1
                # else:
                #     factor = factor+1
        return int(ans)%int(1e9+7)
