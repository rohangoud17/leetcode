class StockPrice:

    def __init__(self):

        self.records = {} # timeStamp -> price
        self.timestamps = []
        self.minHeap = [] #(price, timeStamp)
        self.maxHeap = []


        

    def update(self, timestamp: int, price: int) -> None:
        if timestamp not in self.records:
            self.records[timestamp] = price
        else:
            self.records[timestamp] = price
        heapq.heappush(self.timestamps, -1*timestamp)

        heapq.heappush(self.minHeap, (price, timestamp))
        heapq.heappush(self.maxHeap, (-1*price, timestamp))
        
    def current(self) -> int:

        return self.records[-1*self.timestamps[0]]
        

    def maximum(self) -> int:

        while True:
            price, timestamp = self.maxHeap[0]
            if (self.records[timestamp] == -1*price):
                return -1*price
            heapq.heappop(self.maxHeap)


        return -1*self.maxHeap[0]
        

    def minimum(self) -> int:

        while True:
            price, timestamp = self.minHeap[0]
            if (self.records[timestamp] ==price):
                return price
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()