'''
leetcode: 2187
'''

class Solution(object):
    def minimumTime(self, time, totalTrips):
        """
        :type time: List[int]
        :type totalTrips: int
        :rtype: int
        """
        
            
        n = len(time)
        low,high = 1,max(time)*totalTrips
        
        def check(t):
            trip = 0
            for i in range(n):
                trip = trip + t//time[i]
            if trip>=totalTrips:
                return True
            else:
                return False
        while(low<=high):
            mid = (low+high)//2
            if check(mid):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans
        