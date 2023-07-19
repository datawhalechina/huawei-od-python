# 018_人气最高的店铺

## 题目描述

某购物城有m个商铺，现决定举办一场活动选出人气最高店铺。
活动共有n位市民参与，每位市民只能投一票，但1号店铺如果给该市民发
放q元的购物补贴，该市民会改为投1号店铺。
请计算1号店铺需要最少发放多少元购物补贴才能成为人气最高店铺
（即获得的票数要大于其他店铺），如果1号店铺本身就是票数最高店铺，返回0。

## 输入描述

第一行为小写逗号分割的两个整数n,m,其中第一个整数n表示参与的市民总数，第二个整数m代表店铺总数，1<=n,m<=3000。
第2到n+1行，每行为小写逗号分割的两个整数p,q,表示市民的意向投票情况，其中每行的第一个整数p表示该市民意向投票给p号店
铺，第二个整数q表示其改投1号店铺所需给予的q元购物补贴，1<=p<=m,1<=q<=109。
不考虑输入的格式问题。

## 输出描述

1号店铺需要最少发放购物补贴金额。

## 示例描述

### 示例一

**输入：**
```text
5,5
2,10
3,20
4,30
5,40
5,90
```

**输出：**
```text
50
```

**说明：**  
有5个人参与，共5个店铺。
如果选择发放10元+20元+30元=60元的补贴来抢2,3,4号店铺的票，总共发放了60元补贴(5号店铺有2票，1号店铺要3票才能胜出)
如果选择发放10元+40元=50元的补贴来抢2,5号店铺的票，总共发放了50元补贴（抢了5号店铺的票后，现在1号店铺只要2票就能胜出）
所以最少发放50元补贴

## 解题思路

1. 递归：processVotes函数使用递归来处理投票。它通过不断在变化列表中添加人员并调用自身来生成所有可能的投票情况
2. 回溯：在递归过程中，changeList列表通过添加和移除人员实现回溯。它保存了当前投票情况的状态，并在处理完当前人员后回退
   到上一个状态。
3. 排序：isMax函数中使用了列表的排序功能。它对人气映射中的商店进行排序，以便找到人气最高的商店。
4. 哈希表：popularityMap和tempMap是使用哈希表实现的映射结构，用于存储商店的人气计数。
5. 动态规划（部分）：popularityMap用于保存商店的人气计数，这可以看作是一种动态规划的思想，通过保存子问题的解来减少重
   复计算。
6. 贪心算法（部分）：isMax函数中根据人气值判断是否达到最大值。它首先将人气映射按照人气值降序排序，然后检查人气最高的
   商店是否是商店1，并且是否满足一定的条件，从而进行贪心选择。

## 解题代码

```python
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
```

