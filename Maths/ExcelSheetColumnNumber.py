class Solution(object):
    '''
    Leetcode: 168
    '''
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        ans = ''
        while(columnNumber>26):
            rem = columnNumber%26
            quot = columnNumber//26
            if rem == 0:
                ans = chr(26+64)+ans 
                columnNumber = quot-1
            else:
                ans = chr(rem+64)+ans
                columnNumber = quot
        ans = chr(columnNumber+64)+ans
        return ans

        