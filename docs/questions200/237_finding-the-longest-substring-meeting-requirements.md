# 237 寻找符合要求的最长子串

## 题目描述

给定一个字符串`s`，找出这样一个子串：

1. 该子串中的任意一个字符最多出现2次；
2. 该子串不包含指定某个字符；

请你找出满足该条件的最长子串的长度。

## 输入描述

第一行是要求不包含的指定字符，为单个字符，取值范围`[0-9a-zA-Z]`。 

第二行是字符串`s`，每个字符范围是`[0-9a-zA-Z]`，长度范围是`[1,10000]`。

## 输出描述

一个整数，满足条件的最长子串的长度；如果不存在满足条件的子串，则返回0。

## 示例描述

### 示例一

**输入：**
```
D
ABC123
```

**输出：**
```
6
```

## 解题思路

1. 对字符串使用`split`方法，得到所有不包含指定字符的子串。
2. 遍历子串列表：
    - 使用`Counter`构造字符频次字典。
    - 判断子串的任意字符最多出现2次：如果满足，则将子串加入到结果列表中。
3. 将满足条件的子串按照子串长度从大到小排序。
4. 返回最长的子串，如果结果列表为空，则表示不存在满足条件的子串，返回0。

## 解题代码
```python
from collections import Counter


def solve_method(ch, chars):
    chars_lst = chars.split(ch)

    result = []
    for sub_chars in chars_lst:
        counter = Counter(sub_chars)
        # 判断子串的任意字符最多出现2次
        if all([True if v <= 2 else False for k, v in counter.items()]):
            result.append(sub_chars)

    # 将满足条件的子串按照子串长度从大到小排序
    result.sort(key=lambda x: len(x), reverse=True)
    # 返回最长的子串
    return len(result[0]) if len(result) != 0 else 0


if __name__ == '__main__':
    assert solve_method('D', "ABC123") == 6
    assert solve_method('D', "ABACABD12321") == 5
```