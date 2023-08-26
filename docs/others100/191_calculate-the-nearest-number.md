# 191 计算最接近的数

## 题目描述

给定一个数组`X`和正整数`K`，请找出使表达式`X[i] - X[i+1] - ... - X[i+K-1]`结果最接近于数组中位数的下标`i`，如果有多个`i`满足条件，请返回最大的`i`。

其中，数组中位数是长度为`N`的数组按照元素的值大小升序排列后，下标为`N/2`元素的值。

**补充说明：**

1. 数组`X`的元素均为正整数。
2. `X`的长度`N`取值范围是2 <= N <= 1000。
3. `K`大于0且小于数组的大小。
4. `i`的取值范围是0 <= i < 1000。
5. 题目的排序数组`X[N]`的中位数是`X[N/2]`。

## 输入描述

输入一个数组`X`和正整数`K`。

## 输出描述

输出结果最接近数组中位数的下标`i`，如果有多个`i`满足条件，请返回最大的`i`。

## 示例描述

### 示例一

**输入：**

```text
[1,2,3,3],2
```

**输出：**

```text
2
```

### 示例二

**输入：**

```text
[50,50,2,3],2
```

**输出：**

```text
1
```

**说明：**

中位数为50，`[50,50,2,3]`升序排序后变成`[2,3,50,50]`，中位数为下标`4/2=2`的元素50；

计算结果为1，根据数组`[50,50,2,3]`，按照题目的计算公式`X[i] - X[i+1] - ... - X[i+K-1]`得出三个数：
- X[0] - X[1]= 50 - 50 = 0
- X[1] - X[2] = 50 - 2 = 48
- X[2] - X[3] = 2 - 3 = -1 

其中，48最接近50，因此返回下标1。

## 解题思路

1. `def find_median(nums):`: 定义函数 `find_median`，该函数接受一个数字列表 `nums` 作为参数。
2. `sorted_nums = sorted(nums)`: 将输入的数字列表进行排序，生成一个新的已排序的列表。
3. `N = len(sorted_nums)`: 获取排序后列表的长度。
4. `return sorted_nums[N // 2]`: 返回排序后列表中位于中间位置的数，即中位数。
5. `def main():`: 定义主函数 `main`。
6. 从输入中读取一行字符串，并通过替换操作去除字符串中的一些字符，然后通过逗号分割得到数字字符串列表。
7. `N = len(number_strings) - 1`: 获取数字字符串列表的长度。
8. 将前 `N` 个数字字符串转换为整数列表 `nums`，将最后一个数字字符串转换为整数 `K`。
9. 调用 `find_median(nums)` 计算整个数字列表的中位数。
10. 初始化 `min_distance` 为正无穷大，`index` 为 -1，这两个变量用于记录最小差距和最佳子序列的起始索引。
11. 使用两层循环来寻找符合条件的子序列：

- 外层循环 `i` 从 0 到 `N - K`，用于遍历可能的子序列的起始位置。
- 内层循环 `j` 从 `i + 1` 到 `i + K - 1`，用于计算当前子序列的和。
- 计算当前子序列和的绝对值与中位数之差的距离 `distance`。
- 如果 `distance` 小于 `min_distance`，更新 `min_distance` 和 `index`。

## 解题代码

```python
def find_median(nums):
    sorted_nums = sorted(nums)
    N = len(sorted_nums)
    return sorted_nums[N // 2]


def main():
    input_str = input().replace("[", "").replace("]", "").replace("", "")
    number_strings = input_str.split(",")

    N = len(number_strings) - 1
    nums = [int(x) for x in number_strings[:N]]
    K = int(number_strings[N])

    mid = find_median(nums)
    min_distance = float('inf')
    index = -1
    for i in range(N - K + 1):
        count = nums[i]

        for j in range(i + 1,i+K):
            count -= nums[j]

        distance = abs(count - mid)

        if distance < min_distance:
            min_distance = distance
            index = i
    print(index)


main()
```

