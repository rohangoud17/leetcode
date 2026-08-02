class MedianFinder(object):

    def __init__(self):

        self.small = []
        self.large = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.small, -1*num)
        

        if (self.small and self.large and (-1* self.small[0]) > self.large[0]): # This happens when the largest element in the small heap is bigger than the root of the large heap
            val = -1*heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            
        

        if (self.small and len(self.small) > (len(self.large) + 1)):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if (self.large and len(self.large) > (len(self.small) + 1)):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)
        
       
        

    def findMedian(self):
        """
        :rtype: float
        """
        
        if (len(self.small) > len(self.large)):
            print('1')
            return -1*self.small[0]
        
        if (len(self.small) < len(self.large)):
            return self.large[0]
        
        # print(self.small, self.large)
        
        return ((-self.small[0]) + self.large[0])/2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()