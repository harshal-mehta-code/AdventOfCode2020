def getUpcomingTimeStamps(arrivalTime,busIds):
    timeStamps = {}
    for busId in busIds:
        prevTimeStamp = arrivalTime-(arrivalTime%busId)
        upcomingTime = prevTimeStamp+busId
        timeStamps[busId] = upcomingTime
    return timeStamps

def getWaitingTimes(arrivalTime,timeStamps):
    waitingTimes = {}
    for id in timeStamps:
        waitingTimes[id] = timeStamps[id]-arrivalTime
    return waitingTimes
    
def isConditionMet(timeStamp,busIds):
    result = True
    for busId in busIds:
        if((timeStamp+busId[1])%busId[0]!=0):
            result = result and False
    return result

def getFirstTimeStampWithConsecutiveBuses(busIds):
    busList = [(k,v) for k,v in busIds.items()]
    timeStamp = 0
    jumpSize = busList[0][0]
    nextBusToConsider = 1
    while True:
        if(isConditionMet(timeStamp,busList[:nextBusToConsider+1])):
            jumpSize = timeStamp
            nextBusToConsider +=1
        else:
            timeStamp+=jumpSize
        if(nextBusToConsider>=len(busList)):
            break
    return timeStamp


if __name__ == "__main__":
    with open('testdata.txt') as f:
        arrivalTime = int(f.readline())
        idData = [l for l in f.readline().rstrip().split(',')]
        busIds = {int(l):index for index,l in enumerate(idData) if l!='x'}
    #mostRecentTimeStamps = getUpcomingTimeStamps(arrivalTime,busIds)
    #waitingTimes = getWaitingTimes(arrivalTime,mostRecentTimeStamps)
    #nextBus = min(waitingTimes,key = waitingTimes.get)
    #print(nextBus*waitingTimes[nextBus])
    print(getFirstTimeStampWithConsecutiveBuses(busIds))