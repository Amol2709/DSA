class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s==s[::-1]:
            return s
        max_len = 1
        ans = s[0]

        for i in range(len(s)-1,-1,-1):
            for j in range(i-1,-1,-1):
                if s[j:i+1]==s[j:i+1][::-1]:
                    if max_len<(i-j)+1:
                        max_len = (i-j)+1
                        ans = s[j:i+1]
        return ans


        