# 036 求最大数字

## 题目描述

给定一个由纯数字组成以字符串表示的数值，现要求字符串中的每个数字最多只能出现2次，超过的需要进行删除，删除某个重复的数字后，其它数字相对位置保持不变。

如`34533`，数字3重复超过2次，需要删除其中一个3，删除第一个3后获得最大数值`4533`。

请返回经过删除操作后的最大的数值，以字符串表示。

## 输入描述

第一行为一个纯数字组成的字符串，长度范围：［1，100000］

## 输出描述

输出经过删除操作后的最大的数值

## 示例描述

### 示例一

**输入：**
```text
34533
```

**输出：**
```text
4533
```

### 示例二

**输入：**
```text
5445795045
```

**输出：**
```text
5479504
```
### 示例三

**输入：**
```text
5554
```

**输出：**
```text
554
```

## 解题思路

**基本思路：**
1. 判断每个数字出现的次数。
2. 删除出现次数超过两次的数字，保证字符串中每个数字最多只出现两次。
3. 删除策略为：若当前元素比后一个元素取值小，则可删除当前元素。若没有符合条件的，从后向前依次删除。

**代码思路：**
1. 初始化数字频次字典，`key`为数字，`value`为数字出现的次数。
2. 初始化栈，用于存储第一次删除数字后的结果，从前向后依次删除元素，确保每个元素最多出现两次。
3. 初始化结果列表，用于存储第二次删除数字后的结果，从后向前依次删除元素，确保每个元素最多出现两次。  
4. 返回结果列表组成的字符串。

## 解题代码
```python
from collections import defaultdict


def solve_method(nums):
    num_freq = defaultdict(int)
    for num in nums:
        num_freq[num] += 1

    # 从前向后依次删除元素，确保每个元素最多出现两次
    stack = []
    for num in nums:
        if stack and num_freq[stack[-1]] > 2 and stack[-1] < num:
            num_freq[stack[-1]] -= 1
            stack.pop()
        stack.append(num)

    # 从后向前依次删除元素，确保每个元素最多出现两次
    res = []
    while stack:
        if num_freq[stack[-1]] > 2:
            num_freq[stack[-1]] -= 1
            stack.pop()
        else:
            # 每次都将该数加入到最前面
            res.insert(0, stack.pop())
    return "".join(res)


if __name__ == "__main__":
    # 4533
    # input_str = input().strip()
    # nums = [c for c in input_str]
    # print(solve_method(nums))

    assert solve_method("34533") == "4533"
    assert solve_method("5445795045") == "5479504"
    assert solve_method("5554") == "554"
```