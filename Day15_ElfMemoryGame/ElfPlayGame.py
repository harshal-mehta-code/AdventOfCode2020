class Game:
    def __init__(self,initialNumbers):
        self.Bank = {}
        self.Sequence = []
        for index,num in enumerate(initialNumbers):
            self.Sequence.append(num)
            self.Bank[num] = [index+1,True]
    
    def playGameUntilTurnNumber(self,turnNum):
        while len(self.Sequence)<=turnNum:
            self.takeTurn()
    
    def takeTurn(self):
        prevTurn = len(self.Sequence)
        numberAtPrevTurn = self.Sequence[prevTurn-1]
        numberForCurrentTurn = '0' if self.Bank[numberAtPrevTurn][1] else str(prevTurn - self.Bank[numberAtPrevTurn][0])
        if numberForCurrentTurn in self.Bank:
            self.Bank[numberForCurrentTurn][1] = False
        else:
            self.Bank[numberForCurrentTurn] = [prevTurn+1,True]
        if(self.Bank[numberAtPrevTurn][1]==False):
            self.Bank[numberAtPrevTurn][0] = prevTurn
        self.Sequence.append(numberForCurrentTurn)

    def getNumberAtTurn(self,turnNum):
        return self.Sequence[turnNum-1]

        

if __name__ == "__main__":
    with open('input.txt') as f:
        numbers = [i for i in f.readline().rstrip().split(',')]

    g = Game(numbers)
    g.playGameUntilTurnNumber(30000000)
    print(g.getNumberAtTurn(30000000))