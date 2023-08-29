# 56 子序列长度

## 题目描述

有N个正整数组成的—个序列，给定一个整数sum，求长度最长的的连续子序列使他们的和等于sum返回次子序列的长度，如果没有满足要求的序列返回-1



## 输入描述

两行输入

第一行为﹐拼接的正整数序列

第二行为一个整数sum

## 输出描述

满足条件的子序列的长度，如果没有满足要求的序列返回-1



## 示例描述

### 示例一

**输入：**

```text
1,2,3,4,2
6
```



**输出：**

```text
3
```



## 解题思路

**基本思路：**

1. 双指针遍历（滑动窗口），记录窗口内的值
2. 当值小于target时，不断累加right位置的值
3. 当值大于target时，不断减去left位置的值
4. 当值等于target时，记录此时的长度与最大长度进行比较并且更新

## 解题代码

```python
def solve_method(ints, target_sum):
    max_len = 0  # 初始化最大长度为0

    # 遍历整数列表，寻找和为target_sum的子序列
    for i in range(len(ints)):
        tmp_sum = 0
        for j in range(i, len(ints)):
            tmp_sum += ints[j]
            if tmp_sum > target_sum:
                break
            if tmp_sum == target_sum:
                max_len = max(max_len, j - i + 1)

    return -1 if max_len == 0 else max_len


if __name__ == '__main__':
    # 从输入读取整数列表和目标和
    ints = list(map(int, input().strip().split(',')))
    target_sum = int(input().strip())

    # 调用函数并打印结果
    print(solve_method(ints, target_sum))
```



