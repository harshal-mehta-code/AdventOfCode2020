def getUpcomingTimeStamps(arrivalTime,busIds):
    timeStamps = {}
    for id in busIds:
        prevTimeStamp = arrivalTime-(arrivalTime%id)
        upcomingTime = prevTimeStamp+id
        timeStamps[id] = upcomingTime
    return timeStamps

def getWaitingTimes(arrivalTime,timeStamps):
    waitingTimes = {}
    for id in timeStamps:
        waitingTimes[id] = timeStamps[id]-arrivalTime
    return waitingTimes
     
if __name__ == "__main__":
    with open('input.txt') as f:
        arrivalTime = int(f.readline())
        busIds = [int(id) for id in f.readline().rstrip().split(',') if id!='x']
    mostRecentTimeStamps = getUpcomingTimeStamps(arrivalTime,busIds)
    waitingTimes = getWaitingTimes(arrivalTime,mostRecentTimeStamps)
    nextBus = min(waitingTimes,key = waitingTimes.get)
    print(nextBus*waitingTimes[nextBus])