'''

We have a list A of points (x, y) on the plane. Find the B closest points to the origin (0, 0).

Here, the distance between two points on a plane is the Euclidean distance.

You may return the answer in any order. The answer is guaranteed to be unique
 (except for the order that it is in.)

NOTE: Euclidean distance between two points P1(x1, y1) and P2(x2, y2) is sqrt( (x1-x2)2 + (y1-y2)2 ).
'''

import heapq
class Solution:
    def solve(self, A, B):
        H = []
        heapq.heapify(H)
        for i in range(len(A)):
            x,y = A[i]
            dist = x**2 + y**2
            heapq.heappush(H,(-1*dist, (x,y)))

            if len(H)>B:
                heapq.heappop(H)
        ans = []
        for i in range(len(H)):
            d,point = heapq.heappop(H)
            ans.append(point)
        return ans
        
