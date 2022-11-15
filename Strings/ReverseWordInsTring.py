class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = []
        for i in range(len(s)):
            if s[i]!=' ':
                s = s[i:]
                break
        for i in range(len(s)-1,-1,-1):
            if s[i]!=' ':
                s = s[:i+1]
                break
        p1=p2=0

        while(p2<len(s)):
            if s[p2]!=' ':
                p2+=1
            else:
                ans.append(s[p1:p2])
                for i in range(p2,len(s)):
                    if s[i]!=' ':
                        p1,p2 = i,i
                        break
        ans.append(s[p1:p2+1])
        ans.reverse()
        _ = " ".join(ans)
        return _