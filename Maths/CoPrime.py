
def inlt():
    return(list(map(int,input().split())))
def inp():
    return(int(input()))
import math
t = inp()
for k in range(t):
    n = inp()
    arr = inlt()
    ans = -1
    for i in range(n):
        for j in range(i,n):
            if math.gcd(arr[i],arr[j])==1:
                ans = max(ans,i+j+2)
    print(ans)