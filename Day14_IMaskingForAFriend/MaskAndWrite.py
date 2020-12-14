import parse
import itertools

class Computer:
    def __init__(self):
        self.bitmask = ''
        self.memory = {}

    def clearMemory(self):
        self.memory = {}

    def _setBitMask(self,newMask):
        self.bitmask = newMask

    def _writeToMemoryMasked(self,memAddress,value):
        maskedVal = self._applyMasking(value)
        self._writeToMemory(memAddress,maskedVal)

    def _writeToMemory(self,memAddress,value):
        self.memory[memAddress] = value

    def _applyMasking(self,value):
        binVal = list(format(value,'036b'))
        for index,bit in enumerate(self.bitmask):
            if bit != 'X':
                binVal[index] = bit
        return int("".join(binVal),2)

    def _getMemAddressesFromFloatingAddress(self,floatingAddress):
        bits = '01'
        indices = [i for i,c in enumerate(floatingAddress) if c=='X']
        memAddresses = []
        for t in itertools.product(bits,repeat=len(indices)):
            for i,c in zip(indices,t):
                floatingAddress[i] = c
            memAddresses.append(int(''.join(floatingAddress),2))
        return memAddresses


    def _runMaskingMemoryProtocol(self,memAddress,value):
        floatingAddress = list(format(memAddress,'036b'))
        for index,bit in enumerate(self.bitmask):
            if bit == 'X':
                floatingAddress[index]=bit
            else:
                floatingAddress[index] = str(int(floatingAddress[index])|int(bit))
        memAddresses = self._getMemAddressesFromFloatingAddress(floatingAddress)
        for address in memAddresses:
            self._writeToMemory(address,value)


    def runProgram(self,instructions,version = 'V1'):
        instruction_format = '{} = {}'
        memWrite_format = 'mem[{}]'
        for rawInstruction in instructions:
            parsedInstruction = parse.parse(instruction_format,rawInstruction)
            if(parsedInstruction[0] == 'mask'):
                self._setBitMask(parsedInstruction[1])
            else:
                memAddress = int(parse.parse(memWrite_format,parsedInstruction[0])[0])
                memValue = int(parsedInstruction[1])
                if(version=='V1'):
                    self._writeToMemoryMasked(memAddress,memValue)
                else:
                    self._runMaskingMemoryProtocol(memAddress,memValue)

    def getSumOfMemValues(self):
        return sum(self.memory.values())



if __name__ == "__main__":
    with open('input.txt') as f:
        instructions = [line.rstrip() for line in f.readlines()]

    comp = Computer()
    comp.runProgram(instructions)
    print(comp.getSumOfMemValues())
    comp.clearMemory()
    comp.runProgram(instructions,'V2')
    print(comp.getSumOfMemValues())