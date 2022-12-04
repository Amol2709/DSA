class Solution(object):
    def totalCost(self, costs, k, candidates):
        """
        :type costs: List[int]
        :type k: int
        :type candidates: int
        :rtype: int
        # lc: 2462
        """
        import heapq
        start_minHeap= []
        last_minHeap = []
        
        n= len(costs)
        
        heapq.heapify(start_minHeap)
        heapq.heapify(last_minHeap)
        
        ans = 0
        
        for i in range(candidates):
            heapq.heappush(start_minHeap,(costs[i],i))
            
        remain_elem = min(n-candidates,candidates)
        for i in range(n-1,n-remain_elem-1,-1):
            heapq.heappush(last_minHeap,(costs[i],i))
        
        ptr1= candidates-1
        ptr2 = i
        
        # print(ptr1,ptr2)
        
        while(len(start_minHeap)>0 and len(last_minHeap)>0 and k>0):
            #print(ptr1,ptr2)
            #print(start_minHeap)
            #print(last_minHeap)
            if start_minHeap[0][0]<last_minHeap[0][0]:
                ptr1+=1
                ans+=start_minHeap[0][0]
                heapq.heappop(start_minHeap)
                
                if ptr1<ptr2:
                    heapq.heappush(start_minHeap,(costs[ptr1],ptr1))
            elif start_minHeap[0][0]>last_minHeap[0][0]:
                ptr2-=1
                ans+=last_minHeap[0][0]
                heapq.heappop(last_minHeap)
                if ptr1<ptr2:
                    heapq.heappush(last_minHeap,(costs[ptr2],ptr2))
            else:
                if start_minHeap[0][1]<last_minHeap[0][1]:
                    ptr1+=1
                    ans+=start_minHeap[0][0]
                    heapq.heappop(start_minHeap)
                    
                    if ptr1<ptr2:
                        heapq.heappush(start_minHeap,(costs[ptr1],ptr1))
                else:
                    ptr2-=1
                    ans+=last_minHeap[0][0]
                    heapq.heappop(last_minHeap)
                    
                    if ptr1<ptr2:
                        heapq.heappush(last_minHeap,(costs[ptr2],ptr2))
            k=k-1
        
        if k>0:
            while(len(start_minHeap)>0 and k>0):
                ans = ans + start_minHeap[0][0]
                heapq.heappop(start_minHeap)
                k = k-1
            while(len(last_minHeap)>0 and k>0):
                ans = ans + last_minHeap[0][0]
                heapq.heappop(last_minHeap)
                k = k-1
        return ans
        
        
        