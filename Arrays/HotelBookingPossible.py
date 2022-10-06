class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrival, departure, k):
        ans = []
        n = len(arrival)
        # Create a common vector both arrivals
        # and departures.
        for i in range(0, n):
            ans.append((arrival[i], 1))
            ans.append((departure[i], 0))
    
    
        # Sort the vector
        ans.sort()
        print(ans)
        curr_active, max_active = 0, 0
    
        for i in range(0, len(ans)):
    
            # If new arrival, increment current
            # guests count and update max active
            # guests so far
            if ans[i][1] == 1:
                curr_active += 1
                max_active = max(max_active,
                                curr_active)
    
            # if a guest departs, decrement
            # current guests count.
            else:
                curr_active -= 1
    
        # If max active guests at any instant
        # were more than the available rooms,
        # return false. Else return true.
        return k >= max_active

              
       
      
A = [ 13, 14, 36, 19, 44, 1, 45, 4, 48, 23, 32, 16, 37, 44, 47, 28, 8, 47, 4, 31, 25, 48, 49, 12, 7, 8 ]
B =[ 28, 27, 61, 34, 73, 18, 50, 5, 86, 28, 34, 32, 75, 45, 68, 65, 35, 91, 13, 76, 60, 90, 67, 22, 51, 53 ]
C = 23
obj = Solution()
print(obj.hotel(A,B,C))