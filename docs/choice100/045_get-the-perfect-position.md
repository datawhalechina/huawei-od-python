# 045 获得完美走位

## 题目描述

在第一人称射击游戏中，玩家通过键盘的`A`、`S`、`D`、`W`四个按键控制游戏人物分别向左、向后、向右、向前进行移动，从而完成走位。

假设玩家每按动一次键盘，游戏人物会向某个方向移动一步，如果玩家在操作一定次数的键盘并且各个方向的步数相同时，此时游戏人物必定会回到原点，则称此次走位为完美走位。

现给定玩家的走位（例如：`ASDA`），请通过更换其中一段连续走位的方式使得原走位能够变成一个完美走位。其中待更换的连续走位可以是相同长度的任何走位。请返回待更换的连续走位的最小可能长度。如果原走位本身是一个完美走位，则返回0。

## 输入描述

输入为由键盘字母表示的走位`s`，例如：`ASDA`，其中走位长度的取值范围是1 <= s.length <= 10，`s.length`是4的倍数，`s`中只含有`A`、`S`、`D`、`W`四种字符。

## 输出描述

输出为待更换的连续走位的最小可能长度。

## 示例描述

### 示例一

**输入：**
```text
ASDW
```

**输出：**
```text
0
```

**说明：**  
已经是完美走位了。


### 示例二

**输入：**
```text
AASW
```

**输出：**
```text
1
```

**说明：**  

需要把一个`A`更换成`D`，这样可以得到`ADSW`或者`DASW`。

### 示例三

**输入：**
```text
AAAA
```

**输出：**
```text
3
```

**说明：**  

可以替换后3个`A`，得到`ASDW`。

## 解题思路

1. 初始化每个字符的频数字典`chars`。
2. 更新频数字典，保留缺失的字符。
3. 平衡频数字典`chars`，得到每个字符多出来的个数或缺少的个数。
4. 逐个遍历字符串中的每个字符，并对子串进行更换检查：
   - 持续更换字符，统计更换次数。
   - 检查所有的字符频数是否都为0，如果都为0，则获取更换连续走位的最小长度。
   - 继续遍历字符串中的每个字符。 
5. 返回待更换连续走位的最小长度。

## 解题代码

```python
import math
from collections import Counter


def check(changed_map):
    return all(map(lambda x: False if x > 0 else True, changed_map.values()))


def solve_method(ops):
    chars = {'A': 0, 'S': 0, 'W': 0, 'D': 0}
    length = len(ops)
    count = length // 4
    # 保留缺失的字符
    chars.update(dict(Counter(ops)))
    for k, v in chars.items():
        chars[k] = v - count

    result = math.inf
    for i in range(len(ops)):
        c1 = ops[i]
        res = 0
        changed = chars.copy()
        # 判断当前字符是否多出来
        if changed[c1] > 0:
            # 持续更换字符，统计更换次数
            for j in range(i, length):
                c2 = ops[j]
                changed[c2] -= 1
                res += 1
                # 检查所有的字符频数是否都为0
                if check(changed):
                    break
        if check(changed):
            result = min(result, res)

    return result


if __name__ == '__main__':
    assert solve_method("ASDW") == 0
    assert solve_method("AASW") == 1
    assert solve_method("AAAA") == 3
    assert solve_method("AAADDWWW") == 4
```