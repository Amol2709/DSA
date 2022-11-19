class Solution(object):
    def partitionLabels(self, s):
        """
        leetcode: 763
        :type s: str
        :rtype: List[int]
        """
        starting_map ={}
        ending_map = {}
        n = len(s)
        for i in range(n):
            if s[i] in starting_map:
                starting_map[s[i]]  = min(i,starting_map[s[i]])
            else:
                starting_map[s[i]] = i 
            
            if s[i] in ending_map:
                ending_map[s[i]]  = max(i,ending_map[s[i]])
            else:
                ending_map[s[i]] = i 
        
        curr_min,curr_max = starting_map[s[0]],ending_map[s[0]]
        ans = []
        for i in range(1,n):
            x,y = starting_map[s[i]],ending_map[s[i]]
            if curr_min<=x<=curr_max:
                curr_min = min(curr_min,x)
                curr_max = max(curr_max,y)
            else:
                #print(s[i])
                ans.append(curr_max-curr_min+1)
                curr_min,curr_max = x,y
        ans.append(curr_max-curr_min+1)
        return ans


        