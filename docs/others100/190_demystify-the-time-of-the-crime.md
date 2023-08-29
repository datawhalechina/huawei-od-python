# 190 解密犯罪时间

## 题目描述

警察在侦破一个案件时，得到了线人给出的可能犯罪时间，形如`HH:MM`表示的时刻。根据警察和线人的约定，为了隐蔽，该时间是修改过的。

解密规则为：利用当前出现过的数字，构造下一个距离当前时间最近的时刻，则该时间为可能的犯罪时间。每个出现数字都可以被无限次使用。

## 输入描述

形如`HH:SS`字符串，表示原始输入。

## 输出描述

形如`HH:SS`字符串，表示推理处理的犯罪时间。

## 示例描述

### 示例一

**输入：**

```text
20:12
```

**输出：**

```text
20:20
```

### 示例二

**输入：**

```text
23:59
```

**输出：**

```text
22:22
```

## 解题思路

1. 得到时间中出现过的数字，存入列表`nums`中。
2. 得到当前时间的小时`h`和分钟`m`。
3. 得到由这些数字组成的时间，存入列表`lst`中。
4. 如果分钟数不大，可得到当前小时的时刻的最近分钟，返回结果。
5. 如果当前时间的分钟数很大，则得到后面小时的时刻，返回结果。
6. 上述两个条件都不满足，则得到第二天的最近时刻的最小分钟数，返回结果。

## 解题代码

```python
def solve_method(time):
    # 得到时间中出现过的数字
    nums = [int(c) for c in time if c != ":"]
    # 得到小时和分钟
    h, m = map(int, time.split(":"))
    lst = set()
    # 得到由这些数字组成的时间
    for i in nums:
        for j in nums:
            if i <= 5:
                lst.add(i * 10 + j)
    lst = list(sorted(lst))

    # 当前小时的时刻的最近分钟
    for i in lst:
        if i <= m:
            continue
        return format_time(h, i)

    # 当前时间的分钟数很大，则是后面小时的时刻
    if h != 23:
        for i in lst:
            if i <= h:
                continue
            if i <= 23:
                # 得到最近小时的时刻最小分钟数
                return format_time(i, lst[0])

    # 第二天的最近时刻的最小分钟数
    return format_time(lst[0], lst[0])


def format_time(h, m):
    return f"{h:02d}:{m:02d}"


if __name__ == "__main__":
    assert solve_method("20:12") == "20:20"
    assert solve_method("23:59") == "22:22"
    assert solve_method("20:59") == "22:00"
    assert solve_method("23:09") == "23:20"
```

