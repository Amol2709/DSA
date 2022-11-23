class Solution(object):
    def minimumJumps(self, forbidden, a, b, x):
        """
        # LC: 1654
        :type forbidden: List[int]
        :type a: int
        :type b: int
        :type x: int
        :rtype: int
        """

        from collections import deque

        Q = deque()
        jmp = 0
        visPos = set()
        visPos.add((0,False))

        forbidden = set(forbidden)
        Q.append((0,False))

        while(Q):
            for _ in range(len(Q)):
                curr_pos,isprevstep_backward = Q.popleft()

                if curr_pos == x:
                    return jmp
                

                
                # forward 
                if (curr_pos+a,False) not in visPos and curr_pos+a not in forbidden and curr_pos+a<=6000:
                    Q.append((curr_pos+a,False))
                    visPos.add((curr_pos+a,False))



                #backward 
                if not isprevstep_backward and (curr_pos-b,True) not in visPos and curr_pos-b>=0 and curr_pos-b not in forbidden:
                    Q.append((curr_pos-b,True))
                    visPos.add((curr_pos-b,True))
            
            jmp+=1


        return -1

