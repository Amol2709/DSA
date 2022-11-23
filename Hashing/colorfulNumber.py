'''
What is a COLORFUL Number:

A number can be broken into different contiguous sub-subsequence parts. 
Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245. 
And this number is a COLORFUL number, since product of every digit of a 
contiguous subsequence is different.

'''


class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        s = set()
        num_  = str(A)
        for i in range(len(num_)):
            if int(num_[i]) in s:
                return 0
            s.add(int(num_[i]))
            num = int(num_[i])
            for j in range(i+1,len(num_)):
                num = num*int(num_[j])
                if num in s:
                    return 0
                s.add(num)
        return 1



