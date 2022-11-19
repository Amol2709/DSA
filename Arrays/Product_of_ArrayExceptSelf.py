class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lhs = [1]
        N=len(nums)
        
        for i in range(N):
            lhs.append(lhs[-1]*nums[i])
        rhs=[1]*(N+1)
        for i in range(N-1,-1,-1):
            rhs[i]=rhs[i+1]*nums[i]
        Ans=[]
        for i in range(N):
            Ans.append(lhs[i]*rhs[i+1])
        return Ans