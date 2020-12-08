import copy
def ExecutecCodeAndGetAccValue(instructionList):
    accValue = 0
    index = 0
    while not instructionList[index][1][1]:
        if(instructionList[index][0] == 'acc'):
            accValue+=instructionList[index][1][0]
            instructionList[index][1][1] = True
            index+=1
        elif(instructionList[index][0] == 'jmp'):
            instructionList[index][1][1] = True
            index+=instructionList[index][1][0]
        else:
            index+=1
        
        if(index >= len(instructionList)):
            break
    return accValue,index

def ExecuteAllPotentialFixesAndFindAccValue(allPossibleInstructionSet,exitIndex):
    for fix in allPossibleInstructionSet:
        accValue,lastIndex = ExecutecCodeAndGetAccValue(copy.deepcopy(fix))
        if lastIndex==exitIndex:
            return accValue
    return -1

def GetAllPossibleInstructionSets(instructionList):
    allPossibleInstructionSet = []
    for index,instructionData in enumerate(instructionList):
        if(instructionData[0]=='jmp'):
            newInstructionSet = instructionList[:index]+[['nop',instructionList[index][1]]]+instructionList[index+1:]
            allPossibleInstructionSet.append(newInstructionSet)
        elif(instructionData[0]=='nop'):
            newInstructionSet = instructionList[:index]+[['jmp',instructionList[index][1]]]+instructionList[index+1:]
            allPossibleInstructionSet.append(newInstructionSet)
        else:
            pass
    return allPossibleInstructionSet

if __name__ == "__main__":
    instructionList = []
    with open('input.txt') as f:
        for line in f:
            (instruction,value)  = line.split()
            instructionList.append([instruction,[int(value),False]])
    
    allPossibleInstructionSet = GetAllPossibleInstructionSets(instructionList)
    accVal,_ = ExecutecCodeAndGetAccValue(copy.deepcopy(instructionList))
    print("Acc value after initial run : %d" %accVal)
    print("Acc value after fixing the code : %d" %ExecuteAllPotentialFixesAndFindAccValue(allPossibleInstructionSet,len(instructionList)))