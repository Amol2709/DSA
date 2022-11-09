class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        map_={}
        for word in strs:
            key= ''.join(sorted(word))
            if key in map_:
                map_[key].append(word)
            else:
                map_[key]=[word]
        ans = []
        for key in map_.keys():
            ans.append(map_[key])
        return ans
            
        