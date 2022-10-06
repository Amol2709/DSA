'''
Leetcode:56
'''


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals)
        x,y = intervals[0][0], intervals[0][1]
        ans = []
        
        for i in range(1,len(intervals)):
            if x<=intervals[i][0]<=y:
                y = max(y, intervals[i][1])
            else:
                ans.append([x,y])
                x,y = intervals[i][0],intervals[i][1]
        ans.append([x,y])
        return ans