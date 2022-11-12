class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for i in range(len(s)-1,-1,-1):
            if s[i]==')':
                count = 1
                for j in range(i-1,-1,-1):
                    if s[j]==')':
                        count+=1
                    else:
                        count-=1
                    if count ==0:
                        ans  = max(ans,i-j+1)
                    if count<0:
                        break
        return ans
                

        