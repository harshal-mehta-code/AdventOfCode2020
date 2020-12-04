def makeTreeMap(lines):
    return [[char for char in row.rstrip()] for row in lines]
def countTreesInMap(treeMap,rightSlope,downSlope):
    colCount = rightSlope
    rowCount = downSlope
    numOfTrees = 0
    colBound = len(treeMap[0])
    while(rowCount<=len(treeMap)-1):
        if(treeMap[rowCount][colCount%colBound]=='#'):
            numOfTrees+=1
        rowCount+=downSlope
        colCount=(colCount+rightSlope)%colBound
    return numOfTrees

if __name__ == "__main__":
    with open('input.txt') as f:
        lines = f.readlines()
    treeMap = makeTreeMap(lines)
    totalNumOfTrees = countTreesInMap(treeMap,1,1) * countTreesInMap(treeMap,3,1) * countTreesInMap(treeMap,5,1) * countTreesInMap(treeMap,7,1) * countTreesInMap(treeMap,1,2)
    print(totalNumOfTrees)