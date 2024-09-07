balls = int(input())
totalruns = int(input())
runsscored = int(input())
ballsboweld = int(input())
totalovers = int(balls/6)
overfinished = (ballsboweld//6)+((ballsboweld % 6)/10)
currentrunrate = runsscored/overfinished
totalrunrate = totalruns/totalovers
print(totalovers)
print(overfinished)
print(round(currentrunrate, 1))
print(round(totalrunrate, 1))
if (currentrunrate > totalrunrate):
    print("Eligible to Win")
else:
    print("Not Eligible to Win")
