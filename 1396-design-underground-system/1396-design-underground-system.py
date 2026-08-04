class UndergroundSystem(object):

    def __init__(self):
        self.startMap = {} #id -> (startStation, t)
        self.TotalMap = {} #(startStation, endStation) -> (totalTime, count)
        

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.startMap[id] = (stationName, t)
        

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """

        

        startStation, time = self.startMap[id]
        route = (startStation, stationName)

        if route not in self.TotalMap:
            self.TotalMap[route] = [0,0]
            

        self.TotalMap[route][0] += t-time
        self.TotalMap[route][1] += 1
        

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """

        route = (startStation, endStation)

        return float(self.TotalMap[route][0]) / float(self.TotalMap[route][1])

        
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)