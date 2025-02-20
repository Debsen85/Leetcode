#
# @lc app=leetcode id=1396 lang=python3
#
# [1396] Design Underground System
#

# @lc code=start
class UndergroundSystem:

    def __init__(self):
        self.originDestination = {}
        self.identification = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.identification[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startEnd = self.identification[id][0] + "2" + stationName
        totalTime = t - self.identification[id][1]

        if startEnd in self.originDestination:
            self.originDestination[startEnd][0] += totalTime
            self.originDestination[startEnd][1] += 1
        else:
            self.originDestination[startEnd] = [totalTime, 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        startEnd = startStation + "2" + endStation
        return self.originDestination[startEnd][0] / self.originDestination[startEnd][1]

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
# @lc code=end

