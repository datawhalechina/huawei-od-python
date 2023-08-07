# 037 判断牌型

## 题目描述

五张牌每张牌由牌大小和花色组成
牌大小`2~1 J Q K A`
花色四种 `红桃 黑桃 梅花 方块` 四种花色之一

- 判断牌型

    - 牌型一 同花顺
同一花色的顺子 如红桃 2 红桃 3 红桃 4 红桃 5 红桃 6

    - 牌型二 四条
四张相同数字+单张 红桃 A黑桃 A 梅花 A方块 A 黑桃 A

    - 牌型三 葫芦
三张相同数字加一对
如红桃 5黑桃 5 梅花 5 加方块 9 梅花 9

    - 牌型四 同花
同一种花色
如方块 3 方块 7方块 10 方块 J

    - 牌型五 顺子
花色不一样的顺子
如红桃 2 黑桃 3 红桃 4 红桃 5 方块 6

    - 牌型六 三条
三张相同 + 两张单

    - 牌型七 其他

## 输入描述

输入由 5 行组成
每行为一张牌大小和花色
牌大小为 `2~10 J Q K A`
花色分别用字符 `H S C D` 表示红桃 黑桃 梅花 方块

## 输出描述

输出牌型序号
五张牌符合多种牌型时，取最大的牌型序号输出
五张牌中不会出现数字大小和花色完全相同的牌
编号小的牌型较大，包含`A`的合法顺子只有 `10 J Q  K A`、`A 2 3 4 5`
类似 `KA234` 不是合法顺子

## 示例描述

### 示例一

**输入：**

```Plain Text
4 H
5 S
6 C
7 D
8 D
```

**输出：**

```Plain Text
5
```

### 示例二

**输入：**

```Plain Text
9 S
5 S
8 S
```

**输出：**

```Plain Text
4
```



## 解题思路

**基本思路：** 根据题目模拟，具体看解法，如果存在就返回相应的牌型，不存在返回 0

注意：同花顺：同花和顺子两个条件同时成立即可

## 解题代码

```Python
# 同花
def check_tonghua(colors):
    # 判断花色是否一致
    return len(set(colors)) == 1

# 顺子
def check_shunzi(cards, nums):
    if ("".join(nums) == "2345A"):
        return True
    # 检查是否构成顺子
    for i in range(1, len(nums)):
        if (cards[nums[i - 1]] + 1 != cards[nums[i]]):
            return False
 
    return True
 

 
# 四条
def check_four(nums):
    num_count = {}

    # 统计牌的数量
    for num in nums:
        if num in card_count:
            num_count[num] += 1
        else:
            num_count[num] = 1

    # 检查是否存在四张相同牌值的牌
    values = list(num_count.values())
    return len(values) == 2 and 4 in values

  
 
# 葫芦
def check_hulu(nums):
    num_count = {}

    # 统计牌的数量
    for num in nums:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1

    # 检查是否存在三张相同牌值的牌和两张相同牌值的牌
    values = list(num_count.values())
    return len(values) == 2 and (2 in values or 3 in values)
  
 
 
# 三条
def check_three(nums):
    num_count = {}
    # 统计牌的数量
    for num in nums:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1
    # 判断是否有三张相同牌值得牌
    return any(count == 3 for count in num_count.values())


def main(nums,colors):
    cards ={"2": 2,"3": 3,"4": 4,"5": 5,"6": 6,"7": 7,"8": 8,"9": 9,"10": 10,"J": 11,"Q": 12,"K": 13,"A": 14}
    nums = sorted(nums, key=lambda x: cards[str(x)])
    if (check_shunzi(cards, nums) and check_tonghua(colors)):
        return 1
    elif (check_sitiao(nums)):
        return 2
    elif (check_hulu(nums)):
        return 3
    elif (check_tonghua(colors)):
        return 4
    elif (check_shunzi(cards, nums)):
        return 5
    elif (check_three(nums)):
        return 6
    else:
        return 0
 
if __name__ == "__main__":
    nums = []
    colors = []
    while True:
        poker = [x for x in input().split(" ")]
        if len(poker) >= 2:
            nums.append(poker[0])
            colors.append(poker[1])
        else:
            # 用户输入为空，跳出循环
            break

    res = main(nums,colors)
    print(res)
```

