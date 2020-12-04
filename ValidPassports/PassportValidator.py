import re

def isPassportValid(passPortData):
    Required_Fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
    extractedFields = ''.join(re.findall(r'.{3}:',passPortData))
    return all(item in extractedFields for item in Required_Fields)

def isByrValid(value):
    return (int(value) in range(1920,2003))

def isIyrValid(value):
    return (int(value) in range(2010,2021))

def isEyrValid(value):
    return (int(value) in range(2020,2031))

def isHgtValid(value):
    if(len(value)<=2):
        return False
    elif(value[-2:]=='cm'):
        return (int(value[:-2]) in range(150,194))
    elif(value[-2:]=='in'):
        return (int(value[:-2]) in range(59,77))
    else:
        return False

def isHclValid(value):
    if(len(value)!=7):
        return False
    else:
        return bool(re.match(r'#[a-f0-9]{6}',value))

def isEclValid(value):
    validColors = set(['amb','blu','brn','gry','grn','hzl','oth'])
    return (value in validColors)

def isPidValid(value):
    if(len(value)!=9):
        return False
    else:
        return bool(re.match(r'[0-9]{9}',value))

def isPassportValidWithFields(passPortData):
    if(not isPassportValid(passPortData)):
        return False
    else:
        extractedFields = re.findall(r'.{3}:[^\s]*',passPortData)
        isPassportFullyValid = True
        for item in extractedFields:
            data = item.split(':')
            field = data[0]
            value = data[1]
            if(field=='byr'):
                isPassportFullyValid = isPassportFullyValid and isByrValid(value)
            elif(field=='iyr'):
                isPassportFullyValid = isPassportFullyValid and isIyrValid(value)
            elif(field=='eyr'):
                isPassportFullyValid = isPassportFullyValid and isEyrValid(value)
            elif(field=='hgt'):
                isPassportFullyValid = isPassportFullyValid and isHgtValid(value)
            elif(field=='hcl'):
                isPassportFullyValid = isPassportFullyValid and isHclValid(value)
            elif(field=='ecl'):
                isPassportFullyValid = isPassportFullyValid and isEclValid(value)
            elif(field=='pid'):
                isPassportFullyValid = isPassportFullyValid and isPidValid(value)
            else:
                isPassportFullyValid = isPassportFullyValid and True
        return isPassportFullyValid

def numberOfValidPassports(listOfPassports):
    count = 0
    for passport in listOfPassports:
        if(isPassportValidWithFields(passport)):
            count+=1
    return count

if __name__ == "__main__":
    passportData = []
    with open('input.txt') as f:
        lines = f.readlines()
        currentPassport = ""
        for line in lines:       
            if(line=="\n"):
                passportData.append(currentPassport)
                currentPassport = ""
            else:
                currentPassport = currentPassport+line
    print(numberOfValidPassports(passportData))