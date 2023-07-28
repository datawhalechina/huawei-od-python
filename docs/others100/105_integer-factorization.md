# 105 整数分解

## 题目描述

一个整数可以由连续的自然数之和来表示。给定一个整数，计算该整数有几种连续自然数之和的表达式，并打印出每一种表达式。

## 输入描述

一个目标整数`t`，其中1 <= t <= 100。

## 输出描述

1. 该整数的所有表达式和表达式的个数，如果有多种表达式，自然数个数最少的表达式优先输出。
2. 每个表达式中按自然数递增输出。
   

具体的格式参见样例：在每个测试数据结束时，输出一行`Result:X`，其中X是最终的表达式个数。

## 示例描述

### 示例一

**输入：**

```text
9
```

**输出：**

```text
9=9
9=4+5
9=2+3+4
Result:3
```

**说明：**  
整数9有三种表达方法

### 示例二

**输入：**

```text
10
```

**输出：**

```text
10=10
10=1+2+3+4
Result:2
```

## 解题思路

**基本思路：** 使用贪心算法，遍历取数范围，满足连续整数和等于目标整数`t`，得到表达式。

### 解法一

1. 使用贪心算法，遍历取数范围，对整数的一半向上取整，并逆序取数，因为后面的数不符合要求
    - 根据当前值，顺序取数。
    - 如果连续整数和`sum_num`等于目标整数`t`，表达式的个数累加，则将表达式放入结果列表中。
2. 将表达式的个数放入结果列表中。
3. 返回结果列表。

### 解法二

1. 使用贪心算法，遍历取数范围，对整数的一半向上取整，并逆序取数，因为后面的数不符合要求
    - 根据当前值，按照等差数列求和公式，计算满足目标整数`t`的连续整数个数。
> 计算公式如下：  
> 根据等差数列求和公式，等差数列从$i$到$i+m-1$，等差为1，计算该等差数列的和：
> $$(i + i + m - 1) * m / 2 = t$$
> 推导公式如下：
> $$
\begin{aligned}
& m^2 + (2i - 1) m = 2t \\
\Rightarrow & (m + (2i - 1)/2)^2 = 8t + (2i -1)^2 / 4 \\
\Rightarrow & m + (2i - 1)/2 = \sqrt{8t + (2i -1)^2 / 4} \\
\Rightarrow & m = \sqrt{8t + (2i -1)^2 / 4} - (2i - 1)/2 \\
\Rightarrow & m = \frac{\sqrt{8t + (2i - 1)^2} - 2i + 1}{2}
\end{aligned}
$$
> 
    - 判断上述计算公式中的$m$值是否为整数，如果是整数，则表达式的个数累加，将表达式放入结果列表中。
2. 将表达式的个数放入结果列表中。
3. 返回结果列表。

## 解题代码

### 解法一

```python
import math


def solve_method(t):
    result = []
    result.append("{}={}".format(t, t))
    count = 1
    # 对整数的一半向上取整 因为后面的数没有可能是答案
    for i in range(math.ceil(t / 2) - 1, 0, -1):
        sum_num = i
        expression = "{}={}".format(t, i)
        for j in range(i + 1, math.ceil(t / 2) + 1):
            sum_num += j
            expression = expression + "+" + str(j)
            if sum_num == t:
                result.append(expression)
                count += 1
                break

    result.append("Result:{}".format(count))
    return result

if __name__ == "__main__":
    assert solve_method(9) == ["9=9", "9=4+5", "9=2+3+4", "Result:3"]
    assert solve_method(10) == ["10=10", "10=1+2+3+4", "Result:2"]
```

### 解法二

```python
import math

def solve_method(t):
    result = []
    result.append("{}={}".format(t, t))
    count = 1
    # 对整数的一半向上取整 因为后面的数没有可能是答案
    for i in range(math.ceil(t / 2) - 1, 0, -1):
        # 利用等差数数列公式求解，应为m要求大于零所以排除一个解
        m = ((8 * t + (2 * i - 1) ** 2) ** .5 - 2 * i + 1) / 2
        if m.is_integer():
            count += 1
            result.append("{}={}".format(t, "+".join(map(str, range(i, i + int(m))))))
    result.append("Result:{}".format(count))
    return result

if __name__ == "__main__":
    assert solve_method(9) == ["9=9", "9=4+5", "9=2+3+4", "Result:3"]
    assert solve_method(10) == ["10=10", "10=1+2+3+4", "Result:2"]
```

