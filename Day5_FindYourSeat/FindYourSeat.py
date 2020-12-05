import math
def getSeatIdFromRowCol(row,col):
    return row*8 + col

def getSeatIdFromBoardingPass(boardingPass):
    rowLow, rowHigh = 0, 127
    colLow, colHigh = 0, 7
    selectedRow, selectedCol = 0,0
    passList = [c for c in boardingPass]
    rowData = passList[:7]
    colData = passList[-3:]
    for rowLetter in rowData:
        rowLow,rowHigh,selectedRow = rangeDissector('F','B',rowLetter,rowLow,rowHigh)
    for colLetter in colData:
        colLow,colHigh,selectedCol = rangeDissector('L','R',colLetter,colLow,colHigh)
    return getSeatIdFromRowCol(selectedRow,selectedCol)
    
def rangeDissector(lowLetter,highLetter,currentLetter,lowVal,highVal):
    selectedVal = 0
    if(currentLetter==lowLetter):
        highVal = max(math.floor((lowVal+highVal)/2),lowVal)
        selectedVal = highVal
    elif(currentLetter==highLetter):
        lowVal = min(math.ceil((lowVal+highVal)/2),highVal)
        selectedVal = lowVal
    else:
        pass
    return lowVal,highVal,selectedVal 

def findMissingSeatId(seatIDs):
    seatIDs.sort()
    return (set(range(seatIDs[0],seatIDs[-1]+1))-set(seatIDs))
    
if __name__ == "__main__":
    with open('input.txt') as f:
        boardingPasses = [line.rstrip() for line in f]
    seatIDs = [getSeatIdFromBoardingPass(boardingPass) for boardingPass in boardingPasses]
    print("Max seatID is : " + str(max(seatIDs)))
    print("My seatID is : " + str(findMissingSeatId(seatIDs)))