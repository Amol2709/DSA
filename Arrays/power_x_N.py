class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        # 2^10 = (2*2)^5
        # 4 ^5 = 4 * 4^4
        """
        ans = 1
        if n<0:
            n =-1*n
            x = 1/x
        while(True):
            if n==0:
                return ans
            if n%2==0:
                x = x*x
                n = n//2
            else:
                ans = ans*x
                n= n-1
                
        