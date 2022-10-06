import math
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        n = len(A)
        map_  = {}
        for i in A:
            if i in map_:
                map_[i] +=1
            else:
                map_[i]=1
        count_ = n//3
        for i in map_:
            if map_[i] >count_:
                return i 
        return -1
