class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        map_ = {}
        ptr1,ptr2 = 0,9

        while(ptr1<n-10+1):
            if s[ptr1:ptr2+1] in map_:
                map_[s[ptr1:ptr2+1]]+=1
            else:
                map_[s[ptr1:ptr2+1]]=1
            
            ptr2+=1
            ptr1+=1
        ans = []
        for k in map_:
            if map_[k]>=2:
                ans.append(k)
        return ans

            
        
        