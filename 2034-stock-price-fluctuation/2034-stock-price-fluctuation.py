class StockPrice(object):

    def __init__(self):

        self.records = {} #records = timestamp -> price
        self.timestamps = []
        self.minHeap = [] #(price, timestamp)
        self.maxHeap = [] #(price, timestamp)
        
        
    def update(self, timestamp, price):
        """
        :type timestamp: int
        :type price: int
        :rtype: None
        """

        self.records[timestamp] = price
        heapq.heappush(self.timestamps,-1* timestamp)
        heapq.heappush(self.minHeap, (price,timestamp))
        heapq.heappush(self.maxHeap, (-1*price, timestamp))
                

    def current(self):
        """
        :rtype: int
        """
        return self.records[-1*self.timestamps[0]]
        

    def maximum(self):
        """
        :rtype: int
        """

        while(self.maxHeap and -1* self.maxHeap[0][0] != self.records[self.maxHeap[0][1]]):
            heapq.heappop(self.maxHeap)
        
        return -1*self.maxHeap[0][0]
        

    def minimum(self):
        """
        :rtype: int
        """

        while(self.minHeap and self.minHeap[0][0] != self.records[self.minHeap[0][1]]):
            heapq.heappop(self.minHeap)

        return self.minHeap[0][0]
        
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()



