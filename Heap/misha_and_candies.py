'''
Misha loves eating candies. She has been given N boxes of Candies.

She decides that every time she will choose a box having the minimum number of candies,
 eat half of the candies and put the remaining candies in the other box that has the minimum 
 number of candies.
Misha does not like a box if it has the number of candies greater than B 
so she won't eat from that box. Can you find how many candies she will eat?

NOTE 1: If a box has an odd number of candies then Misha will eat the floor(odd / 2).

NOTE 2: The same box will not be chosen again.

'''

import heapq
class Solution:
    def solve(self, A, B):
        heapq.heapify(A)
        ans = 0
        while(len(A)>0):
            x = heapq.heappop(A)
            if x>B:
                break
            candy = x//2

            ans = ans+candy
            remain_candy = x-candy
            if len(A)>0:
                y = heapq.heappop(A)
                heapq.heappush(A,y+remain_candy)
        return ans






