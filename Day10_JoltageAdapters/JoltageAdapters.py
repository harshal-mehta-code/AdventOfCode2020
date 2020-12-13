from collections import Counter
from itertools import combinations
import copy

def CalculateJoltDifferences(joltAdapterList):
    diffList = [t-s for s,t in zip(joltAdapterList,joltAdapterList[1:])]
    return Counter(diffList)

    
def isArrangementValid(adapterList):
    for i in range(1,len(adapterList)-1):
        if not (1<=adapterList[i]-adapterList[i-1]<=3):
            break
    return (i==(len(adapterList)-2))

def getAllDitchableAdapters(adapterList):
    ditchableAdapters = []
    for i in range(1,len(adapterList)-1):
        if (adapterList[i+1]-adapterList[i-1]<=3):
            ditchableAdapters.append(adapterList[i])
    return ditchableAdapters

def getNumberOfValidAdapterSequences(adapterList,ditchableAdapters):
    numberOfValidSequences = 0
    validSequences = set()
    for i in range(0,len(ditchableAdapters)+1):
        possibleCombinations = [comb for comb in combinations(ditchableAdapters,i)]
        for comb in possibleCombinations:
            testList = copy.deepcopy(adapterList)
            for item in comb:
                testList.remove(item)
            if(isArrangementValid(testList)):
                numberOfValidSequences+=1
                validSequences.add(tuple(testList))
    return numberOfValidSequences,validSequences
            

if __name__ == "__main__":
    with open('input.txt') as f:
        joltAdapterList = sorted(list(map(int,f)))
    joltAdapterList = [0] + joltAdapterList + [max(joltAdapterList)+3] 
    joltDifferences = CalculateJoltDifferences(joltAdapterList)
    print(joltDifferences[1],joltDifferences[3])
    ditchableAdapters = getAllDitchableAdapters(joltAdapterList)
    numSeq,Seqs = getNumberOfValidAdapterSequences(joltAdapterList,ditchableAdapters)
    print(len(Seqs))