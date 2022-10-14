
'''
Given a string A and a dictionary of words B, 
add spaces in A to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

Input 1:
    A = "catsanddog",
    B = ["cat", "cats", "and", "sand", "dog"]

Output 1:
    ["cat sand dog", "cats and dog"]
'''

class Solution:
    def wordBreak(self, A, B):
        self.bSet = set(B)
        self.A = A 
        self.n = len(A)

        self.ans = []
        self.myFunc(0,"")
        return self.ans
    def myFunc(self,index,tmp):
        if index>=self.n:
            if tmp[0]==" ":
                tmp = tmp[1:]
            self.ans.append(tmp)
            return
        for i in range(index,self.n):
            if self.A[index:i+1] in self.bSet:
                self.myFunc(i+1,tmp+" "+self.A[index:i+1])
