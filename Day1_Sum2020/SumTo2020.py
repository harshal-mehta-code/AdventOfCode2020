import math
def getPairThatSumsToNum(nums,sumNum):
    left = 0
    right = len(nums)-1
    pairList = []
    while(left<right):
        if(nums[left]+nums[right] > sumNum):
            right-=1
        elif(nums[left]+nums[right] < sumNum):
            left+=1
        else:
            pairList.append(nums[left])
            pairList.append(nums[right])
            break
    return pairList
        
if __name__ == "__main__":
    with open('input.txt') as f:
        nums = [int(x) for x in f.read().split()]
    # sort list
    nums.sort()
    subPair = []
    for index,item in enumerate(reversed(nums)):
        subPair = getPairThatSumsToNum(nums[:-(index+1)],2020-item)
        if(len(subPair)!=0):
            print(subPair,item,math.prod(subPair)*item)
