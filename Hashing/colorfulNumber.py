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



