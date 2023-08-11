# 096 数大雁

## 题目描述

一群大雁往南飞，给定一个字符串，记录地面上的游客听到的大雁叫声，请给出叫声最少由几只大雁发出。

具体的：
1. 大雁发出的完整叫声为`quack`，因为有多只大雁同一时间嘎嘎作响，所以字符串中可能会混合多个`quack`。
2. 大雁会依次完整发出`quack`，即字符串中`q`、`u`、`a`、`c`、`k`这5个字母，按顺序完整存在才能计数为一只大雁。如果不完整或者没有按顺序则不予计数。
3. 如果字符串不是由`q`、`u`、`a`、`c`、`k`字符组合而成，或者没有找到一只大雁，请返回-1。

## 输入描述

一个字符串，包含大雁`quack`的叫声。字符串长度的取值范围是1 <= 字符串长度 <= 1000，字符串中的字符只有`q`、`u`、`a`、`c`、`k`。

## 输出描述

大雁的数量。

## 示例描述

### 示例一

**输入：**
```text
quackquack
```

**输出：**
```text
1
```

### 示例二

**输入：**
```text
qaauucqcaa
```

**输出：**
```text
-1
```

### 示例三

**输入：**
```text
quacqkuack
```

**输出：**
```text
2
```

## 解题思路

**基本思路：** 建立大雁的桶，该桶用来描述大雁的叫声，统计大雁叫声的重叠数。
1. 初始化桶，统计大雁叫声的重叠数。
2. 初始化大雁计数器。
3. 遍历字符串：
   - 如果字符与`q`相等，则相应位置累加1。
   - 如果不相等，获取字符在`quack`中的索引，并将前一个字符的计数减1，后一个字符的计数加1。
   - 如果计数中存在-1，说明字符顺序不正确，返回-1。
   - 更新大雁计数器为当前计数的最大值，统计大雁的叫声重叠数。 
4. 如果计数不为0，说明字符数量不匹配，返回-1。
5. 返回大雁计数器的结果。

## 解题代码

```python
def solve_method(chars):
    if len(chars) % 5 != 0:
        return -1

    quack_str = "quack"
    # 建立桶
    bucket = [0] * len(quack_str)
    # 大雁计数器
    count = 0

    for char in chars:
        if char == quack_str[0]:
            # 如果字符与`q`相等，则相应位置累加1
            bucket[0] += 1
        else:
            # 获取字符在`quack`中的索引
            index = quack_str.index(char)
            # 将前一个字符的计数减1，后一个字符的计数加1
            bucket[index - 1] -= 1
            bucket[index] += 1
            if char == quack_str[-1]:
                bucket[-1] -= 1

        if -1 in bucket:
            # 如果计数中存在-1，说明字符顺序不正确，返回-1
            return -1
        # 更新大雁计数器为当前计数的最大值，统计大雁的叫声重叠数
        count = max(count, sum(bucket))

    if sum(bucket) != 0:
        # 如果计数不为0，说明字符数量不匹配，返回-1
        return -1

    return count


if __name__ == '__main__':
    assert solve_method("quackquack") == 1
    assert solve_method("qaauucqcaa") == -1
    assert solve_method("quacqkuack") == 2
```