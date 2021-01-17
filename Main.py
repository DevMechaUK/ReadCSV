resultList = []

def readFile():
    resultFile = open('Results.csv', 'r')
    for line in resultFile:
        line = line.rstrip("\n")
        line = line.split(",")
        resultList.append(line)
    resultFile.close
    del resultList[0]
    del resultList[0]
    return resultList

readFile()

for i in range(len(resultList)):
    print("Team:" + resultList[i][0] + " Played:" + resultList[i][1]
          + " Won:" + resultList[i][2] + " Draw:" + resultList[i][3])
