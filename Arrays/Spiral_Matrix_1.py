class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        r,c = len(matrix),len(matrix[0])
        top,bottom,left,right = 0,r-1,0,c-1
        ans = []
        count = 0
        while(count<r*c):
            if count<r*c:
                for i in range(left,right+1):
                    ans.append(matrix[top][i])
                    count  = count +1
                top = top+1
            if count<r*c:
                for i in range(top,bottom+1):
                    ans.append(matrix[i][right])
                    count = count+1
                right = right -1
            if count<r*c:
                for i in range(right,left-1,-1):
                    ans.append(matrix[bottom][i])
                    count = count+1
                bottom = bottom-1
            if count<r*c:
                for i in range(bottom,top-1,-1):
                    ans.append(matrix[i][left])
                    count = count+1
                left = left+1
        return ans
        