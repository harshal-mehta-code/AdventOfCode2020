class Ship:
    def __init__(self):
        self.North = 0
        self.East = 0
        self.South = 0
        self.West = 0
        self.HeadingDirection = 'East'
        self.Waypoint = self.Waypoint()

    class Waypoint:
        def __init__(self):
            self.North = 1
            self.East = 10
            self.South = 0
            self.West = 0
            self.WaypointDirection = ['North','East']
        
        def updateDirectionValues(self,primaryDir,secondaryDir,value):
            setattr(self,primaryDir,getattr(self,primaryDir)+abs(min(getattr(self,secondaryDir)-value,0)))
            setattr(self,secondaryDir,max(getattr(self,secondaryDir)-value,0))
            self.WaypointDirection = []
            for direction in ['North','South','East','West']:
                if(getattr(self,direction)!=0):
                    self.WaypointDirection.append(direction)


        def changeWaypointDirection(self,offsetIndex):
            directions = ['North','East','South','West']
            oldValues = []
            for index,direction in enumerate(self.WaypointDirection):
                newDirection = directions[(directions.index(direction)+offsetIndex)%len(directions)]
                oldValues.append(getattr(self,direction))
                setattr(self,direction,0)
                self.WaypointDirection[index] = newDirection

            for oldval,newdirection in zip(oldValues,self.WaypointDirection):
                setattr(self,newdirection,oldval)
            
        
        def getShipMovingInstructions(self,value):
            shipMovingInstructions = [('N',value*self.North),('E',value*self.East),('S',value*self.South),('W',value*self.West)]
            return shipMovingInstructions


    def moveWaypoint(self,instruction):
        if(instruction[0]=='F'):
            shipMovingInstructions = self.Waypoint.getShipMovingInstructions(instruction[1])
            for shipInstruction in shipMovingInstructions:
                self.moveShip(shipInstruction)
        elif(instruction[0]=='N'):
            self.Waypoint.updateDirectionValues('North','South',instruction[1])
        elif(instruction[0]=='S'):
            self.Waypoint.updateDirectionValues('South','North',instruction[1])
        elif(instruction[0]=='E'):
            self.Waypoint.updateDirectionValues('East','West',instruction[1])
        elif(instruction[0]=='W'):
            self.Waypoint.updateDirectionValues('West','East',instruction[1])
        elif(instruction[0]=='L'):
            self.Waypoint.changeWaypointDirection(-instruction[1]//90)
        elif(instruction[0]=='R'):
            self.Waypoint.changeWaypointDirection(instruction[1]//90)
        else:
            pass

    def moveShip(self,instruction):
        if(instruction[0]=='F'):
            self.updateDirectionValues(self.HeadingDirection,Ship.getOppositeDirection(self.HeadingDirection),instruction[1])
        elif(instruction[0]=='N'):
            self.updateDirectionValues('North','South',instruction[1])
        elif(instruction[0]=='S'):
            self.updateDirectionValues('South','North',instruction[1])
        elif(instruction[0]=='E'):
            self.updateDirectionValues('East','West',instruction[1])
        elif(instruction[0]=='W'):
            self.updateDirectionValues('West','East',instruction[1])
        elif(instruction[0]=='L'):
            self.changeHeadingDirection(int(-instruction[1]/90))
        elif(instruction[0]=='R'):
            self.changeHeadingDirection(int(instruction[1]/90))
        else:
            pass
            
    def printShipPosition(self):
        print("North: {}, East: {}, South: {}, West: {}".format(self.North,self.East,self.South,self.West))

    def changeHeadingDirection(self,offsetIndex):
        directions = ['North','East','South','West']
        newDirection = directions[(directions.index(self.HeadingDirection)+offsetIndex)%len(directions)]
        self.HeadingDirection = newDirection

    def updateDirectionValues(self,primaryDir,secondaryDir,value):
        setattr(self,primaryDir,getattr(self,primaryDir)+abs(min(getattr(self,secondaryDir)-value,0)))
        setattr(self,secondaryDir,max(getattr(self,secondaryDir)-value,0))

    def getManhattanDistance(self):
        return self.North+self.South+self.East+self.West

    @staticmethod
    def getOppositeDirection(direction):
        dirMapping = {'North':'South','East':'West','South':'North','West':'East'}
        return dirMapping[direction]

if __name__ == "__main__":
    with open('input.txt') as f:
        instructions = [(line.rstrip()[0],int(line.rstrip()[1:])) for line in f.readlines()]
    s = Ship()
    for instruction in instructions:
        s.moveWaypoint(instruction)
    s.printShipPosition()    
    print(s.getManhattanDistance())