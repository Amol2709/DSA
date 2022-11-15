class Solution:
    '''
    2447
    '''
    def subarrayGCD(self, nums, k) :
        import math
        n = len(nums)
        count = 0
        for i in range(n):
            elem = nums[i]
            if nums[i]==k:
                count+=1
            for j in range(i+1,n):
                elem  = math.gcd(nums[j],elem)
                print(elem)
                if elem ==k:
                    count+=1
        return count

