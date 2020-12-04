import re

def isPasswordValid_policy1(occurenceRange, letterToCheck, password):
    return password.count(letterToCheck) in range(occurenceRange[0],occurenceRange[1]+1)

def isPasswordValid_policy2(occurenceIndices, letterToCheck, password):
    return (password[occurenceIndices[0]-1]==letterToCheck)^(password[occurenceIndices[1]-1]==letterToCheck)

def parseLineIntoSegments(line):
    segments = line.split(" ")
    occurenceRange = [int(x) for x in segments[0].split("-")]
    letterToCheck = re.sub(r'\W+', '', segments[1])
    password = segments[2]
    return (occurenceRange,letterToCheck,password)
if __name__ == "__main__":
    validPasswordCount = 0
    with open('input.txt','r') as f:
        for line in f:
            line = line.strip()
            passwordData = parseLineIntoSegments(line)
            if(isPasswordValid_policy2(passwordData[0],passwordData[1],passwordData[2])):
                validPasswordCount+=1
    print(validPasswordCount)