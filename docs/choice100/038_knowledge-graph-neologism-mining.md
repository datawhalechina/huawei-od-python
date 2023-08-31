# 038 知识图谱新词挖掘

## 题目描述
小华负责公司知识图谱产品，现在要通过新词挖掘完善知识图谱。
- 新词挖掘：给出一个待挖掘文本内容字符串`content`和一个词的字符串`word`，找到`content`中所有`word`的新词。
- 新词：使用词`word`的字符排列形成的字符串。

请帮小华实现新词挖掘，返回发现的新词的数量。

## 输入描述

第一行输入为待挖掘的文本内容`content`；
第二行输入为词`word`；

取值范围是：
- 0 <= content.length <= 10000000
- 1 <= word.length <= 2000

## 输出描述

在`content`中找到的所有`word`的新词的数量。

## 示例描述

### 示例一

**输入：**
```text
qweebaewqd
qwe
```

**输出：**
```text
2
```

**说明：**  

起始索引等于0的子串是`qwe`，它是`word`的新词。  
起始索引等于6的子串是`ewq`，它是`word`的新词。



### 示例二

**输入：**
```text
abab
ab
```

**输出：**
```text
3
```

**说明：**

起始索引等于0的子串是`ab`，它是`word`的新词。 
起始索引等于1的子串是`ba`，它是`word`的新词。 
起始索引等于2的子串是`ab`，它是`word`的新词。

## 解题思路

**基本思路：** 使用滑动窗口求解。
1. 滑动窗口大小为字符串`word`的长度。
2. 创建字符串`word`的`Counter`对象`c2`。
3. 遍历字符串`content`的长度：
    - 创建滑动窗口内`content`子串的`Counter`对象`c1`。
    - 比较两个对象，如果相等，统计结果加1。
4. 返回统计结果。

## 解题代码

```python
from collections import Counter


def solve_method(content: str, word: str) -> int:
    w = len(word)
    count = 0
    c2 = Counter(word)

    for i in range(len(content) - w + 1):
        c1 = Counter(content[i:i + w])
        if c1 == c2:
            count += 1

    return count


if __name__ == '__main__':
    assert solve_method("qweebaewqd", "qwe") == 2
    assert solve_method("abab", "ab") == 3
```