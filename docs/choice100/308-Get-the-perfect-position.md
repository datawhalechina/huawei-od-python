# 308 获得完美走位

## 题目描述
在第一人称射击游戏中，玩家通过键盘的 `A、S、D、W` 四个按键控制游戏人物分别向左、向后、向右、向前进行移动，从而完成走位。 \
假设玩家每按动一次键盘，游戏人物会向某个方向移动一步，如果玩家在操作一定次数的键盘并且各个方向的步数相同时，此时游戏人物必定会回到原点，则称此次走位为完美走位。 \
现给定玩家的走位（例如：`ASDA`）,请通过更换其中一段连续走位的方式使得原走位能够变成一个完美走位。 \
其中待更换的连续走位可以是相同长度的任何走位。 \
请返回待更换的连续走位的最小可能长度。 \
若果原走位本身是一个完美走位，则返回0。

## 输入描述
1. 输入为由键盘字母表示的走位 `s`，例如：`ASDA`
走位长度 $1≤s.length≤10$ 
2. s.length 是 4 的倍数
3. s 中只含有 `A, S, D, W` 四种字符

## 输出描述
输出为待更换的连续走位的最小可能长度

### 示例一
**输入：**
```shell
ASDW
```

**输出：**
```shell
0
```

**说明：**  
已经是完美走位了。


### 示例二
**输入：**
```shell
AASW
```

**输出：**
```shell
1
```

**说明：**  
需要把一个 `A` 更换成 `D`，这样可以得到 `ADSW` 或者 `DASW`。

### 示例三
**输入：**
```shell
AAAA
```

**输出：**
```shell
3
```

**说明：**  
可以替换后 3 个 `A`，得到 `ASDW`。

## 解题思路
最重要的是使用双重循环，对列表 chars 中的每个字符都执行以下操作： \
- 如果当前字符的数量 (在字典 c_count 中的值)大于 0，则对其他字符进行处理。
- 遍历列表 chars，并累加处理字符数量，在每次处理后检查所有字符的数量是否都小于等于 0
- 如果所有字符的数量都小于等于 0，则更新最小值 ( min_ ) 。
## 解题代码

```python
# 输入获取
s = input()
 
 
# 算法入口
def getResult(s):
    # 此时count记录统计W,A,S,D字母的数量
    count = {
        "W": 0,
        "A": 0,
        "S": 0,
        "D": 0
    }
 
    for c in s:
        count[c] += 1
 
    avg = len(s) / 4  # 平衡状态时，W,A,S,D应该都是avg数量
    total = 0  # total用于记录多余字母个数
    flag = True  # flag表示当前是否为平衡状态，默认是
 
    for c in count.keys():
        if count[c] > avg:
            flag = False  # 如果有一个字母数量超标，则平衡打破
            count[c] -= avg  # 此时count记录每个字母超过avg的数量
            total += count[c]
        else:
            count[c] = 0
 
    if flag:
        return 0  # 如果平衡，则输出0
 
    i = 0
    j = 0
    minLen = len(s) - 1
 
    while j < len(s):
        jc = s[j]
 
        if count[jc] > 0:
            total -= 1
        count[jc] -= 1
 
        while total == 0:
            minLen = min(minLen, j - i + 1)
 
            ic = s[i]
            if count[ic] >= 0:
                total += 1
            count[ic] += 1
 
            i += 1
 
        j += 1
 
    return minLen
 
 
print(getResult(s))
```