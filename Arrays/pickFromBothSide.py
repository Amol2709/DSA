class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        sum_=0
        for i in range(0,B):
            sum_=sum_+A[i]
        count_=-1
        temp_=0
        ans=sum_
        for i in range(B-1,-1,-1):
            sum_=(sum_-A[i])
            temp_=temp_+A[count_]
            count_=count_-1
            ans = max(ans,sum_+temp_)
            
        return ans
            
        
