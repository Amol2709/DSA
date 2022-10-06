class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        low,high = 0,A 

        while(low<=high):
            mid = (low+high)//2
            tmp = mid**2

            if tmp==A:
                return mid
            elif tmp >A:
                high = mid-1
            else:
                low = mid+1
        return high
