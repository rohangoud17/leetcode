class UndergroundSystem:

    def __init__(self):
        self.startMap = {} #id -> (startStation, t)
        self.TotalMap = {} #(startStation, endStation) -> [totalTime, count]
        

    def checkIn(self, id: int, startStation: str, t: int) -> None:

        self.startMap[id] = (startStation, t)
        

    def checkOut(self, id: int, endStation: str, t: int) -> None:

        startStation, time = self.startMap[id]

        route = (startStation, endStation)

        if route not in self.TotalMap:
            self.TotalMap[route] = [0,0]
        
        self.TotalMap[route][0] += t - time
        self.TotalMap[route][1] += 1
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:

        route = (startStation, endStation)

        return self.TotalMap[route][0]/self.TotalMap[route][1]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)