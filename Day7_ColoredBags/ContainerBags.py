import re

def GetOuterAndInnerBagData(rules):
    pOuterBag = re.compile(r'(.*)\sbags\scontain')
    pInnerBags = re.compile(r'([\d]\s[a-zA-z]*\s[a-zA-Z]+)')
    outerBags = [pOuterBag.match(rule).group(1) for rule in rules]
    innerBagData = [pInnerBags.findall(rule) for rule in rules]
    return outerBags,innerBagData

def BuildDictionaryFromBagData(outerBags,innerBagData):
    bagDict = {}
    for outerBag,innerBagList in zip(outerBags,innerBagData):
        bagDict[outerBag] = BuildInnerBagDictionary(innerBagList)
    return bagDict

def BuildInnerBagDictionary(innerBagList):
    innerBagDict = {}
    for innerBagItem in innerBagList:
        match = re.match(r'(\d+)\s(\w+\s\w+)',innerBagItem)
        innerItems = match.groups()
        innerBagDict[innerItems[1]] = innerItems[0]
    return innerBagDict
        
def GetBagAncestors(bagDict, innerBagColor):
    bagAncestors = GetBagParents(bagDict,innerBagColor)
    for bagAncestor in bagAncestors:
        bagAncestors = bagAncestors.union(GetBagAncestors(bagDict,bagAncestor))
    return bagAncestors

def GetBagParents(bagDict,innerBagColor):
    bagParents = set()
    for bag in bagDict:
        if innerBagColor in bagDict[bag]:
            bagParents.add(bag)
    return bagParents

def CountChildrenBags(bagDict,mainBagColor):
    childrenBagDict = bagDict[mainBagColor]
    totalBags = 1
    for childBag in childrenBagDict:
        totalBags += int(childrenBagDict[childBag])*CountChildrenBags(bagDict,childBag)
    return totalBags

if __name__ == "__main__":
    with open('input.txt') as f:
        rules = f.readlines()
    outerBags,innerBagData = GetOuterAndInnerBagData(rules)
    bagDict = BuildDictionaryFromBagData(outerBags,innerBagData)
    bagAncestors = GetBagAncestors(bagDict,'shiny gold')
    print("Shiny gold bag can be contained within %d other bags" %len(bagAncestors))
    print("To carry shiny gold bag, you need to carry %d bags in total" %(CountChildrenBags(bagDict,'shiny gold')-1))