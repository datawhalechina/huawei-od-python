from collections import defaultdict

popularityMap =defaultdict(int)
minMoney = float("inf")
money = 0
def processVotes(peopleList,changeList,index):
    global minMoney,money
    if isMax(changeList) and minMoney > money:
        minMoney = money
    else:
        for i in range(index,len(peopleList)):
            changeList.append(peopleList[i])
            processVotes(peopleList,changeList,i+1)
            changeList.pop()
def isMax(changeList):
    global popularityMap,money
    tempMap = popularityMap.copy()
    money = 0
    for shop,popularity in changeList:
        money +popularity
        tempMap[shop]-=1
        tempMap[1]+=1
    entryList = sorted(tempMap.items(),key=lambda x:x[1],reverse=True)
    firstShop = entryList[0][0]
    if firstShop == 1 and (len(entryList) == 1 or entryList[0][1]>entryList[1][1]):
        return True
    return False
if __name__=="__main__":
    input1 = input().split(",")
    shopCount = int(input1[0])
    voteCount = int(input1[1])
    peopleList = []
    popularityMap[1]=0
    for i in range(shopCount):
        input2 = input().split(",")
        shop = int(input2[0])
        popularity = int(input2[1])
        if shop != 1:
            peopleList.append([shop,popularity])
        popularityMap[shop]+1
    processVotes(peopleList,[],0)
    print(minMoney)