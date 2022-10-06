class Solution:
    def checkRow(self):
        for i in range(0,9):
            s = set()
            for elem in self.A[i]:
                if elem =='.':
                    continue
                if elem in s:
                    return False
                s.add(elem)
        return True
    def checkCol(self):
        for i in range(0,9):
            s = set()
            for j in range(0,9):
                if self.A[j][i] == '.':
                    continue 
                if self.A[j][i] in s:
                    return False 
                s.add(self.A[j][i])
        return True
    def checkBox(self):
        for i in range(0,9,3):
            for j in range(0,9,3):
                s = set()
                for row in range(i,i+3):
                    for col in range(j,j+3):
                        if self.A[row][col] == '.':
                            continue
                        if self.A[row][col] in s:
                            return False
                        s.add(self.A[row][col])
        return True
    def isValidSudoku(self, A):
        self.A = A
        if self.checkBox() and self.checkCol() and self.checkRow():
            return 1
        else:
            return 0

