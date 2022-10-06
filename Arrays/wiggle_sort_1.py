'''
arrange the elements into a sequence such that

a1 >= a2 <= a3 >= a4 <= a5..... 

T.C = O[nlogn]
'''
def wave(self, A):
    A.sort()
    for i in range(1,len(A),2):
        A[i],A[i-1]=A[i-1],A[i]
    return A