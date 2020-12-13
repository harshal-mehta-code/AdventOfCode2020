from collections import Counter
import copy
import numpy

def getNumOfOccupiedSeats(seats):
    counts = list(map(Counter,seats))
    return sum([count['#'] for count in counts])
        
def getNeighbors(seats,i,j):
    return numpy.array([seats[i-1][j-1],seats[i-1][j],seats[i-1][j+1],seats[i][j-1],seats[i][j+1],seats[i+1][j-1],seats[i+1][j],seats[i+1][j+1]])

def ApplySittingRules(seats,ruleType):
    getRequiredNeighbors = (getNeighbors if ruleType=='Old' else getFirstVisibleNeighborInEachDirection)
    adjacentSeatThreshold = (4 if ruleType=='Old' else 5)
    numOfChangedSeats = 0
    numCols = len(seats[0])
    numRows = len(seats)
    updatedArrangement = copy.deepcopy(seats)

    for i in range(1,numRows-1):
        for j in range(1,numCols-1):
            if(seats[i][j]=='L'):
                neighbors = getRequiredNeighbors(seats,i,j)
                if not '#' in neighbors:
                    updatedArrangement[i][j]='#'
                    numOfChangedSeats+=1
            elif(seats[i][j]=='#'):
                neighbors = getRequiredNeighbors(seats,i,j)
                if(Counter(neighbors)['#']>=adjacentSeatThreshold):
                    updatedArrangement[i][j]='L'
                    numOfChangedSeats+=1
            else:
                pass
    return updatedArrangement,numOfChangedSeats

def printSeatConfig(seats):
    for row in seats:
        print(row)

def getNumOfOccupiedSeatsAfterChaosSettles(seats,ruleType):
    arrangement = seats
    while True:
        arrangement,numOfChangedSeats = ApplySittingRules(arrangement,ruleType)
        if(numOfChangedSeats==0):
            break
    return getNumOfOccupiedSeats(arrangement)
    
def getFirstVisibleNeighborInEachDirection(seats,I,J):
    firstVisibleNeighbors = []
    right = seats[I,J+1:]
    left = seats[I,:J][::-1]
    up = seats[:I,J][::-1]
    down = seats[I+1:,J]
    
    visibleNeighborList = [right,left,up,down,upLeft,downRight,upRight,downLeft]
    for direction in visibleNeighborList:
        for neighbor in direction:
            if(neighbor!='.'):
                firstVisibleNeighbors.append(neighbor)
                break
    return firstVisibleNeighbors
    
if __name__ == "__main__":
    with open('testinput.txt') as f:
        lines = f.readlines()
    seats = numpy.array([[l for l in line.rstrip()] for line in lines])
    #add padding for ease of calculation
    seats = numpy.pad(seats,pad_width=1,mode='constant',constant_values='.')
    print("Number of occupied seats according to initial rules: %d"%getNumOfOccupiedSeatsAfterChaosSettles(seats,'Old'))
    print("Number of occupied seats according to new rules: %d"%getNumOfOccupiedSeatsAfterChaosSettles(seats,'New'))