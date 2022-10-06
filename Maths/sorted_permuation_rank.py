'''
Given a string, S find the rank of the string amongst all its permutations sorted lexicographically.
The rank can be big. So print it modulo 1000003. 
Note: Return 0 if the characters are repeated in the string.
'''



def rank(A):
        if len(A)!=len(set(A)):
            return 0
        # code here
        import math
        n = len(A)
        map = {}
        alive_char = list(range(n))
        total_alive = n
        sorted_str = sorted(A)
        
        
        for i in range(n):
            map[sorted_str[i]]=i 
        rank = 0
        for i in range(n):
            rank = rank+ (( alive_char[map[A[i]]] * math.factorial(total_alive-1) ) % (1e6+3))
            for j in range(map[A[i]],n):
                alive_char[j] = alive_char[j]-1
            total_alive = total_alive-1
        rank = int((rank+1) % (1e6+3))
        return rank
