class Solution(object):
    def findAnagrams(self, s, p):
        """
        Leetcode: 438
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        map_p = {}
        map_s = {}
        for i in p:
            if i in map_p:
                map_p[i]+=1
            else:
                map_p[i]=1
        
        n = len(p)
        ans = []
        p1=p2=0
        while(p2<len(s)):
            if s[p2] in map_s:
                map_s[s[p2]]+=1
            else:
                map_s[s[p2]]=1
            
            if p2-p1+1==n:
                if map_p==map_s:
                    ans.append(p1)
                map_s[s[p1]]-=1
                if map_s[s[p1]]==0:
                    del map_s[s[p1]]
                p1+=1
            
            p2+=1

                
        return ans
        