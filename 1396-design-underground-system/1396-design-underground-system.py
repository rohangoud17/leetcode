class UndergroundSystem:

    def __init__(self):

        self.startMap = {} # id-> (startStation, time)
        self.totalMap = {} # (startStation, endStation) -> [noOfTravelers, TotalTimeTraveled]
        
    def checkIn(self, id: int, startStation: str, t: int) -> None:

        self.startMap[id] = (startStation, t)
        

    def checkOut(self, id: int, endStation: str, t: int) -> None:

        route =  (self.startMap[id][0], endStation)
        timeTaken = t - self.startMap[id][1] 
        
        
        if route in self.totalMap:
            self.totalMap[route][0] += 1
            self.totalMap[route][1] += timeTaken
        else:
            self.totalMap[route] = [1, timeTaken]
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:

        route = (startStation, endStation)
        av = 0

        if route in self.totalMap:
            av = self.totalMap[route][1]/self.totalMap[route][0]
        
        return av
        
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)