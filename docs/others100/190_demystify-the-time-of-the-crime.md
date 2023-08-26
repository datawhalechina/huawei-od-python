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

这段代码实现的是给定一个24小时格式的时间字符串，返回下一个最小的有效时间，其中有效时间指的是由原始时间中的数字组成的最小的能够表示有效时间的时间，即在小时范围[0,23]内，分钟范围[0,59]内能够组成的最小时间。

代码中的函数 solve_method 接收一个字符串参数time，用于表示输入的时间，返回值为一个字符串，表示下一个最小的有效时间。在函数内部，首先将时间字符串中的数字提取出来并存入 nums 列表中，然后使用 map 函数将小时和分钟转换为整数类型的 h 和 m 变量。接着，通过两层循环将可能的时间存入 lst 列表中，并进行排序。

## 解题代码

```python
def solve_method(time: str) -> str:
    nums = [int(c) for c in time if c !=":"]
    h , m = map(int, time.split(":"))
    lst = []
    for i in nums:
        for j in nums:
            if i <= 5:
                lst.append(i * 10 + j)
    lst.sort()
    for i in lst:
        if i <= m:
            continue
        return format_time(h, i)
    if h != 23:
        for i in lst :
            if i <= h:
                continue
            if i <= 23:
                return format_time(i, lst[0])
    return format_time(lst[0],lst[0])

def format_time(h: int, m: int) -> str:
    return f"{h:02d}:{m:02d}"

if __name__ == "__main__":
    t = input()
    ret = solve_method(t)
    print(ret)
```

