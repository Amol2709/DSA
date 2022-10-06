class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def addArrays(self, A, B):
        num1,num2 = "",""
        for i in range(len(A)):
            num1 = num1+str(A[i])
        for j in range(len(B)):
            num2 = num2 + str(B[j])
        
        ans = str(int(num1)+int(num2))
        L = []
        for i in ans:
            L.append(int(i))
        return L
        
