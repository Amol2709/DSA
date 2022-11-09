class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        p1=p2 = 0
        ans = 1
        flag = 1
        map_={}
        while(p2<len(s) and p1<=p2):
            if s[p2] not in map_:
                map_[s[p2]]=p2
                p2=p2+1
                ans = max(ans,p2-p1)
            else:
                flag = 0
                p1 = max(p1,map_[s[p2]]+1)
                map_[s[p2]]=p2
                p2=p2+1
                ans = max(ans,p2-p1)
            
            
        if flag ==1:
            return len(s)
        return ans
        