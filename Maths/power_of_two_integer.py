'''
Given a positive integer which fits in a 32 bit signed integer, 
find if it can be expressed as A^P where P > 1 and A > 0.
 A and P both should be integers.
'''

def isPower(self, A):
    if A==0:
        return 0
    if A==1:
        return 1
    n = (A//2)+1
    for i in range(2,n):
        y=2
        while(True):
            elem = i**y
            if elem==A:
                return 1
            if elem>A:
                break
            y = y+1
    return 0