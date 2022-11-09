class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        for i in range(0,A+1):
            tmp=[]
            for j in range(0,i+1):
                if j==0 or j == i:
                    tmp.append(1)
                else:
                    tmp.append(prev_row[j]+prev_row[j-1])
            prev_row = tmp
        return prev_row
