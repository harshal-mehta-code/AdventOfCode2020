def initialize():
    with open('testdata.txt') as data:
        return [line.strip() for line in data]

class Boat():
    def __init__(self):
        self.position = [0,0]
        self.compass = {'N':[1,1],'E':[0,1],'S':[1,-1],'W':[0,-1]}        
            
    def advance(self,move,waypoint):
        for x in range(move.value):
            self.position[0] += waypoint.position_to_ship[0]
            self.position[1] += waypoint.position_to_ship[1]
    
    def distance(self):
        return abs(self.position[0])+abs(self.position[1])
        
        
class Move():
    def __init__(self,move):
        self.type = move[0]
        self.value = int(move[1:])
        
class Waypoint():
    def __init__(self):
        self.position_to_ship = [10,1]
        
    def move(self,move):
        if move.type == 'N':
            self.position_to_ship[1] += move.value
            return
        elif move.type == 'S':
            self.position_to_ship[1] -= move.value
            return
        elif move.type =='E':
            self.position_to_ship[0] += move.value
            return
        elif move.type =='W':
            self.position_to_ship[0] -= move.value
            return
        else:
            print('ERROR!')
    
    def rotate(self,move):
        rotations = int(move.value/90)
        if move.type == 'L':
            x_rotation_seed = -1
            y_rotation_seed = 1
        if move.type == 'R':
            x_rotation_seed = 1
            y_rotation_seed = -1
        for x in range(rotations):
            self.position_to_ship = [x_rotation_seed*self.position_to_ship[1],self.position_to_ship[0]*y_rotation_seed]
            if x+1%2 == 0:
                x_rotation_seed *= -1
                y_rotation_seed *= -1

def main():
    b = Boat()
    w = Waypoint()
    directions = initialize()
    
    for direction in directions:
        
        move = Move(direction)
        if move.type in b.compass:
            w.move(move)
        elif move.type == 'F':
            b.advance(move,w)
        elif move.type in 'LR':
            w.rotate(move)
            
    return (b.distance())

print(main())
