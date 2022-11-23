class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        LC: 455
        """
        g,s = sorted(g,reverse = True),sorted(s,reverse = True)

        n1,n2 = len(g),len(s)
        ptr1,ptr2= n1-1,n2-1
        ans = 0
        while(ptr1>=0 and ptr2>=0):
            if s[ptr2]>=g[ptr1]:
                ptr1-=1
                ptr2-=1
                ans+=1
            else :
                ptr2-=1
        return ans
                

