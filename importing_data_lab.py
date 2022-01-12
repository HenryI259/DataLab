import csv

maxTemp = 0
minTemp = 0
averageMax = 0
averageMin = 0
dataAmount = 0
first = True

with open('Norman2016.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        max = float(row['TMAX'])
        min = float(row['TMIN'])
        if max > 120 or min < -80:
            continue
        
        if first:
            maxTemp = max
            minTemp = min
            first = False

        if max > maxTemp:
            maxTemp = max
        if min < minTemp:
            minTemp = min
        
        averageMax += max
        averageMin += min
        dataAmount += 1

averageMax /= dataAmount
averageMin /= dataAmount

print(f"The highest temperature was {round(maxTemp, 2)}")
print(f"The lowest temperature was {round(minTemp, 2)}")
print(f"The average highest temperature was {round(averageMax, 2)}")
print(f"The average lowest temperature was {round(averageMin, 2)}")