class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        stk = []
        for i in range(len(s)):
            if s[i]==']':
                curr_str  = ""
                while(stk[-1]!='['):
                    curr_str=stk.pop()+curr_str
                stk.pop()

                num = ""
                while(stk and stk[-1].isdigit()):
                    num = stk.pop()+num

                stk.append(int(num)*curr_str)
                


            else:
                stk.append(s[i])
        ans = "".join(stk)
        return ans