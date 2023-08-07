# 036 Maximum_value_after_Deletion

## 题目描述

一个 长整型数字，消除重复的数字后，得到最大的一个数字
如 12341，消除重复的 1，可得到 1234 或 2341，取最大值 2341。
42234，消除 4 得到 4223 或者 2234 ，再消除 2，得到 423 或 234，取最大值 423.

## 输入描述

输入一个数字，范围[1,100000]

## 输出描述

输出经过删除操作后的最大值

## 示例描述

### 示例一

**输入：**

```Plain Text
12341
```

**输出：**

```Plain Text
2341
```

### 示例二

**输入：**

```Plain Text
42234
```

**输出：**

```Plain Text
423
```

## 解题思路

**基本思路：** 

1. 创建一个字典`number_count`，遍历`number`统计每个数字出现的频率，同时将数字压入栈res[]中

2. 遍历`number_count`,当键值count≥2时：

    3. 如果后一个位置res[i+1]大于当前位置res[i]，则删除当前位置

    4. 如果是最后一个数字且还有剩余，那么删除最后一个数字

5. 最后返回结果

## 解题代码

```Python
from collections import defaultdict

def solve_method(number):
    # 创建一个字典去统计数字频率
    number_count = defaultdict(int)
    res = []
    for c in number:
        # 相同的数字加一
        number_count[c] += 1
        res.append(c)

    for c, count in number_count.items():
        for i in range(len(res)):
            # 选择>=2的数
            if count < 2:
                break
            if res[i] == c:
                if res[i + 1] > c:
                    res.pop(i)
                    i -= 1
                    count -= 1
                elif i == len(res) - 1:
                    res.pop()
                    count -= 1

    return "".join(res)

if __name__ == "__main__":
    number = input().strip()
    print(solve_method(number))
```

