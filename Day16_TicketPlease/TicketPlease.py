from collections import OrderedDict
from itertools import permutations
import parse
import math
import numpy
import copy

def getSumOfInvalidValuesInNearbyTickets(nearbyTickets,rules):
    invalidNums = []
    allFieldVals = getAllRangesFromAllRules(rules)
    for ticket in nearbyTickets:
        outOfRangeNums = getOutOfRangeNumsForTicket(ticket,allFieldVals)
        for num in outOfRangeNums:
            invalidNums.append(num)
    return sum(invalidNums)

def removeInvalidTickets(nearbyTickets,rules):
    allFieldVals = getAllRangesFromAllRules(rules)
    for ticket in list(nearbyTickets):
        outOfRangeNums = getOutOfRangeNumsForTicket(ticket,allFieldVals)
        if len(outOfRangeNums)!=0:
            nearbyTickets.remove(ticket)

def getAllRangesFromAllRules(rules):
    allFieldVals = []
    for value in rules.values():
        for pair in value:
            allFieldVals.append(pair)
    return allFieldVals
    
def getOutOfRangeNumsForTicket(ticket,allFieldVals):
    invalidNumList = []    
    for ruleVal in ticket:
        if not any(lower <= ruleVal <= upper for (lower,upper) in allFieldVals):
            invalidNumList.append(ruleVal)
    return invalidNumList

def getFieldNameForWhichAllValuesAreValid(fieldVals,rules):
    fieldName = ""
    for rule in rules:
        if all(any(lower<=val<=upper for (lower,upper) in rules[rule]) for val in fieldVals):
            fieldName = rule
            break
    del rules[fieldName]
    return fieldName


def findCorrectRuleOrder(nearbyTickets,rules):
    correctOrder = []
    ticketArray = numpy.array(nearbyTickets)
    testRules = copy.deepcopy(rules)
    for position in range(0,len(ticketArray[0])):
        currentFieldVals = ticketArray[:,position]
        fieldName = getFieldNameForWhichAllValuesAreValid(currentFieldVals,testRules)
        correctOrder.append(fieldName)
    return correctOrder


def areAllTicketsValidForTheRuleOrder(nearbyTickets,rules,order):
    ticketsValid = True
    for ticket in nearbyTickets:
        for val,rule in zip(ticket,order):
            ranges = rules[rule]
            if not any(lower <= val <= upper for (lower,upper) in ranges):
                ticketsValid = False
                return ticketsValid
    return ticketsValid

def getValuesFromFieldNameContaining(myTicket,rulerOrder,fieldWord):
    values = []
    for rule,value in zip(ruleOrder,myTicket):
        if fieldWord in rule:
            values.append(value)
    return values

if __name__ == "__main__":
    with open('testdata2.txt') as f:
        lines = f.readlines()
    ruleList = [l.rstrip() for l in lines[:lines.index('\n')]]
    myTicket = [int(l) for l in lines[lines.index('your ticket:\n')+1].rstrip().split(',')]
    nearbyTickets = [[int(l) for l in line.rstrip().split(',')] for line in lines[lines.index('nearby tickets:\n')+1:]]
    rules = OrderedDict()
    ruleFormat = '{}: {}-{} or {}-{}'
    for ruleLine in ruleList:
        parsedRule = parse.parse(ruleFormat,ruleLine)
        rules[parsedRule[0]] = [(int(parsedRule[1]),int(parsedRule[2])),(int(parsedRule[3]),int(parsedRule[4]))]

    print(getSumOfInvalidValuesInNearbyTickets(nearbyTickets,rules))
    removeInvalidTickets(nearbyTickets,rules)
    ruleOrder = findCorrectRuleOrder(nearbyTickets,rules)
    #values = getValuesFromFieldNameContaining(myTicket,ruleOrder,'departure')
    #print(ruleOrder)