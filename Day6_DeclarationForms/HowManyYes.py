def GetNumberOfAnyYesPerGroup(groups):
    numOfAnyYesPerGroup = []
    for group in groups:
        answers = "".join(group.split('\n'))
        numOfAnyYesPerGroup.append(len(set(answers)))
    return numOfAnyYesPerGroup

def GetNumberOfAllYesPerGroup(groups):
    numOfAllYesPerGroup = []
    for group in groups:
        answerSets = [set(person) for person in group.rstrip().split('\n')]
        numOfAllYesPerGroup.append(len(set.intersection(*answerSets)))
    return numOfAllYesPerGroup
    
if __name__ == "__main__":
    with open('input.txt') as f:
        contents = f.read()
        groups = contents.split('\n\n')
    numOfAnyYesPerGroup = GetNumberOfAnyYesPerGroup(groups)
    numOfAllYesPerGroup = GetNumberOfAllYesPerGroup(groups)
    print(sum(numOfAnyYesPerGroup))
    print(sum(numOfAllYesPerGroup))