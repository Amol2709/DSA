class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arr, dep, K):
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
        n = len(arr)

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

            # Update result if needed
            if (plat_needed > result):
                result = plat_needed
        
        return K>=result