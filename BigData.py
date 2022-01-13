import csv

stationList = []

class stationInfo():
    def __init__(self, name):
        self.name = name
        self.first = True
        self.averageMax, self.averageMin, self.dataAmount = 0, 0, 0

    def cleanData(self, max, min):
        if max > 120 or min < -80:
            return False
        else:
            return True

    def findMaxMin(self, max, min):
        if self.first:
            self.maxTemp = max
            self.minTemp = min
            self.first = False

        if max > self.maxTemp:
            self.maxTemp = max
        if min < self.minTemp:
            self.minTemp = min

    def findAverages(self, max, min):
        self.averageMax += max
        self.averageMin += min
        self.dataAmount += 1

    def printInfo(self):
        self.averageMax /= self.dataAmount
        self.averageMin /= self.dataAmount
        print(f"The highest temperature for the {self.name} station was {round(self.maxTemp, 2)}")
        print(f"The lowest temperature for the {self.name} station was {round(self.minTemp, 2)}")
        print(f"The average highest temperature for the {self.name} station was {round(self.averageMax, 2)}")
        print(f"The average lowest temperature for the {self.name} station was {round(self.averageMin, 2)}")
        print("")

with open('BigData2016.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        max = float(row['TMAX'])
        min = float(row['TMIN'])
        currentStation = row['STID']
        i = 0
        if len(stationList) == 0:
            stationList.append(stationInfo(currentStation))
        for station in stationList:
            i += 1
            if station.name == currentStation:
                break
            else:
                if i >= len(stationList):
                    stationList.append(stationInfo(currentStation))
        for station in stationList:
            if station.name == currentStation:
                if station.cleanData(max, min):
                    station.findMaxMin(max, min)
                    station.findAverages(max, min)

for station in stationList:
    station.printInfo()