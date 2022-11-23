class Solution(object):
    def maximalSquare(self, matrix):
        """
        Lc 221
        :type matrix: List[List[str]]
        :rtype: int
        """
        row,col = len(matrix),len(matrix[0])
        dp  = [[0 for i in range(col)]for j in range(row)]
        ans = 0
        for i in range(0,col):
            dp[0][i] = int(matrix[0][i])
            ans = max(ans,dp[0][i])
        for i in range(0,row):
            dp[i][0] = int(matrix[i][0])
            ans = max(ans,dp[i][0])
        

        for i in range(1,row):
            for j in range(1,col):
                # if i can contribute
                if int(matrix[i][j])==1:
                    if int(matrix[i][j-1]) and int(matrix[i-1][j]) and int(matrix[i-1][j-1]):
                        dp[i][j] = min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1
                    else:
                        dp[i][j] = 1
             
                ans = max(ans,dp[i][j])

        return ans**2