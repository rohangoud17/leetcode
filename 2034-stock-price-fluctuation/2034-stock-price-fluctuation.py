class StockPrice(object):

    def __init__(self):

        self.records = {}
        self.minPriceHeap = [] #(price, timestamp)
        self.maxPriceHeap = []
        self.timeStampsHeap = []
        
    def update(self, timestamp, price):
        """
        :type timestamp: int
        :type price: int
        :rtype: None
        """
        
        heapq.heappush(self.timeStampsHeap, -1* timestamp)
        self.records[timestamp] = price
        heapq.heappush(self.minPriceHeap, (price,timestamp))
        heapq.heappush(self.maxPriceHeap, (-1*price, timestamp))


    def current(self):
        """
        :rtype: int
        """
        if -1* self.timeStampsHeap[0] in self.records:
            return  self.records[-1*self.timeStampsHeap[0]]
        

    def maximum(self):
        """
        :rtype: int
        """
        while (self.maxPriceHeap and -1*self.maxPriceHeap[0][0] != self.records[self.maxPriceHeap[0][1]]):
            heapq.heappop(self.maxPriceHeap)
        
        return -1*self.maxPriceHeap[0][0]

    def minimum(self):
        """
        :rtype: int
        """
        while (self.minPriceHeap[0][0] != self.records[self.minPriceHeap[0][1]]):
            heapq.heappop(self.minPriceHeap)
        
        return self.minPriceHeap[0][0]
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()



