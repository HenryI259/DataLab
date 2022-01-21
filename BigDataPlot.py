import csv
import matplotlib.pyplot as plot

stationList = []

class stationInfo():
    def __init__(self, name):
        self.name = name
        self.averageMax, self.averageMin, self.maxTemp, self.minTemp = 0, 0, 0, 0
        self.info = {
            "Max" : [],
            "Min" : [],
            "Humidity": [],
            "WindMax": [],
            "WindMin": [],
            "Rain": [],
        }
        self.months = []
    
    def cleanData(self, value, limits):
        if value > limits[1] or value < limits[0]:
            return False
        else:
            return True

    def addData(self, infoName, data, limits):
        if self.cleanData(data, limits):
            self.info[infoName].append(data)
        else:
            self.info[infoName].append("")

    def findMax(self, infoName):
        theMax = 0
        for data in self.info[infoName]:
            if data != "":
                if theMax == 0 or data > theMax:
                    theMax = data
        return theMax

    def findMin(self, infoName):
        theMin = 0
        for data in self.info[infoName]:
            if data != "":
                if theMin == 0 or data < theMin:
                    theMin = data
        return theMin

    def findAverage(self, infoName):
        dataAmount = 0
        average = 0
        for data in self.info[infoName]:
            if data != "":
                average += data
                dataAmount += 1

        average /= dataAmount
        return average

    def plotInfo(self, list):
        plot.plot(range(len(list)), list, label = station.name)
        

    def cleanInfo(self, infoName):
        newList = []
        for i in range(len(self.info[infoName])):
            if self.info[infoName][i] == "":
                forwardStep = 1
                while self.info[infoName][i + forwardStep] == "":
                    forwardStep += 1
                if i == 0:
                    info = self.info[infoName][i + forwardStep]
                elif i == len(self.info[infoName]) - 1:
                    info = newList[i - 1]
                else:
                    info = ((self.info[infoName][i + forwardStep] - info) / forwardStep + 1) + info
            else:
                info = self.info[infoName][i]
            newList.append(info)
        return newList

    def findMonth(self, month, list):
        newList = []
        j = 0
        for i in list:
            if int(self.months[j]) == int(month):
                newList.append(i)
            j += 1
        return newList

    def printInfo(self):
        print(f"The highest temperature for the {self.name} station was {round(self.maxTemp, 2)}")
        print(f"The lowest temperature for the {self.name} station was {round(self.minTemp, 2)}")
        print(f"The average highest temperature for the {self.name} station was {round(self.averageMax, 2)}")
        print(f"The average lowest temperature for the {self.name} station was {round(self.averageMin, 2)}")
        print("")

with open('2016VizData.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        max = float(row['TMAX'])
        min = float(row['TMIN'])
        humidity = float(row['HAVG'])
        windMax = float(row['WSMX'])
        windMin = float(row['WSMN'])
        rain = float(row['RAIN'])
        
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
                station.addData("Max", max, (-80, 120))
                station.addData("Min", min, (-80, 120))
                station.addData("Humidity", humidity, (-80, 120))
                station.addData("WindMax", windMax, (-80, 120))
                station.addData("WindMin", windMin, (-80, 120))
                station.addData("Rain", rain, (-80, 120))
                station.months.append(row['MONTH'])

name = input("Hello weather enjoyer, what is your name")
print(f"Hello {name}!")
while True:
    print(f"What data would you like to see")
    data = input("Max, Min, Humidity, WindMax, WindMin, Rain")
    time = input(f"And for what time to do you want see that info (month number, year)")
    print("Ok here is your graph")

    for station in stationList:
        dataList = station.cleanInfo(data)
        try:
            if int(time) in range(11):
                newDataList = station.findMonth(int(time) + 1, dataList)
                station.plotInfo(newDataList)
            else:
                station.plotInfo(dataList)
        except:
            station.plotInfo(dataList)

    plot.legend()
    plot.show()

    if input("Would you like to see another graph? (y/n)") != 'y':
        break