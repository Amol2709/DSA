'''
Surprisingly, in an alien language, they also use English lowercase letters, 
but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given an array of words A of size N written in the alien language, 
and the order of the alphabet denoted by string B of size 26, return 1 if and only
 if the given words are sorted lexicographically in this alien language else, return 0.

 A = ["hello", "scaler", "interviewbit"]
 B = "adhbcfegskjlponmirqtxwuvzy"
o/p=1

  A = ["fine", "none", "no"]
 B = "qwertyuiopasdfghjklzxcvbnm"
 o/p=0
'''

class Solution:
    # @param A : list of strings
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        _map,index = {},1
        for i in range(len(B)):
            _map[B[i]]=i
        def check(index):
            word1,word2 = A[index-1], A[index]
            ptr1, ptr2 = 0,0
            n1,n2 = len(A[index-1]),len(A[index])

            while(ptr1<n1 and ptr2<n2):
                if _map[word1[ptr1]]> _map[word2[ptr2]]:
                    return False
                if _map[word1[ptr1]]< _map[word2[ptr2]]:
                    return True
                
                ptr1+=1
                ptr2+=1
            # if ptr1<n1 or ptr2<n2:
            #     return False
            # return True
        while(index<len(A)):
            if _map[A[index-1][0]] == _map[A[index][0]]:
                if check(index):
                    index = index+1
                else:
                    return 0
            elif _map[A[index-1][0]] < _map[A[index][0]]:
                index = index+1
            else:
                return 0
        return 1
        
       
        
