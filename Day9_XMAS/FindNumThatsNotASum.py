from itertools import combinations

def GetNumThatDoesntSum(numList,preembleSize):
    answer = None
    for i in range(preembleSize,len(numList)):
        preembleList = numList[i-preembleSize:i]
        if not isNumASum(preembleList,numList[i]):
            answer = numList[i]
            break
    return answer

def isNumASum(preembleList,targetNum):
    possibleSums = [sum(comb) for comb in combinations(preembleList,2)]
    return targetNum in possibleSums

def FindContiguousListOfNums(preembleList,targetNum):
    index = preembleList.index(targetNum)
    cappedList = preembleList[:index]
    possibleContiguousLists = [cappedList[i:i+j] for i in range(0,len(cappedList)) for j in range(2,len(cappedList)-i+1)]
    answer = []
    for sublist in possibleContiguousLists:
        if(sum(list(sublist))==targetNum):
            answer = list(sublist)
            break
    return answer

if __name__ == "__main__":
    with open('input.txt') as f:
        numList = [int(line) for line in f.readlines()]
        faultyNum = GetNumThatDoesntSum(numList,25)
        print("Faulty number is : %d" %faultyNum)
        contiguousListOfNums = FindContiguousListOfNums(numList,faultyNum)
        print("Encryption weakness is : %d" %(min(contiguousListOfNums)+max(contiguousListOfNums)))