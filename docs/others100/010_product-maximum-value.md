# 010 乘积最大值

## 题目描述

给定一个元素类型为小写字符串的数组，请计算两个没有相同字符的元素长度乘积的最大值，如果没有符合条件的两个元素，则返回0。

## 输入描述

输入为一个`,`分隔的小写字符串数组，其中2 <= 数组长度 <= 100，0 < 字符串长度 <= 50。

## 输出描述

两个没有相同字符的元素长度乘积的最大值。

## 示例描述

### 示例一

**输入：**
```
iwdvpbn,hk,iuop,iikd,kadgpf
```

**输出：**
```
14
```

**说明：**  
数组中有5个元组，第一个和第二个元素没有相同字符，满足条件，则输出7*2=14。

## 解题思路

1. 初始化最大值`max_value`。
2. 遍历字符串数组：
    - 两两字符串比较：判断字符串的set集合，集合合并的长度是否等于各集合的长度和，如果等于，则表示没有相同字符
    - 计算两个字符串长度的乘积，取最大值。
3. 返回满足条件的最大值。    

## 解题代码

```python
def solve_method(strings):
    max_value = 0
    for i in range(len(strings)):
        for j in range(i, len(strings)):
            set_a = set(strings[i])
            set_b = set(strings[j])
            # 判断set集合合并的长度是否等于各集合的长度和，如果等于，则表示没有相同字符
            if len(set_a.union(set_b)) == len(set_a) + len(set_b):
                max_value = max(max_value, len(set_a) * len(set_b))

    return max_value


if __name__ == '__main__':
    assert solve_method(["iwdvpbn", "hk", "iuop", "iikd", "kadgpf"]) == 14
```

