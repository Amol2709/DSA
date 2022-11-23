
class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # Sort arrival and
        # departure arrays
        arr.sort()
        dep.sort()
        
        # plat_needed indicates
        # number of platforms
        # needed at a time
        plat_needed = 1
        result = 1
        i = 1
        j = 0
        
        # Similar to merge in
        # merge sort to process
        # all events in sorted order
        while (i < n and j < n):
        
            # If next event in sorted
            # order is arrival,
            # increment count of
            # platforms needed
            if (arr[i] <= dep[j]):
        
                plat_needed += 1
                i += 1
        
            # Else decrement count
            # of platforms needed
            elif (arr[i] > dep[j]):
        
                plat_needed -= 1
                j += 1
            result = max(plat_needed,result)
        
        return result