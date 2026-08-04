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


        #since we first push the number directly to small heap, we check if the top of the heap in the small array is larger than the top of the large array 
        if (self.small and self.large and (-1*self.small[0]) > self.large[0]):
            val = -1*heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        
        #checking if both the arrays are equal length or approximately equal
        if (self.small and len(self.small) > (len(self.large) + 1)):
            val = -1* heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if (self.large and len(self.large) > (len(self.small) + 1)):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1*val)



    def findMedian(self):
        """
        :rtype: float
        """

        if (len(self.small) > len(self.large)):
            return -1*self.small[0]

        if (len(self.large) > len(self.small)):
            return self.large[0]
        

        return (self.large[0] + -1*self.small[0])/2.0
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()