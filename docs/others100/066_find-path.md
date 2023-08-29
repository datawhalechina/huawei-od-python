# 066 寻找路径

## 题目描述

二叉树也可以用数组来存储，给定一个数组，树的根节点的值储存在下标1，对于储存在下标`n`的节点，它的左子节点和右子节点分别储存在下标`2n`和`2n+1`，并且我们用-1代表一个节点为空。

给定一个数组存储的二叉树，试求从根节点到最小的叶子节点的路径，路径由节点的值组成。

## 输入描述

输入一行为数组的内容，数组的每个元素都是正整数，元素间用空格分隔。

注意第一个元素即为根节点的值，即数组的第`n`元素对应下标`n`。下标0在树的表示中没有使用，所以我们省略了。输入的树最多为7层。

## 输出描述

输出从根节点到最小叶子节点的路径上各个节点的值，由空格分隔，用例保证最小叶子节点只有一个。

## 示例描述

### 示例一

**输入：**
```text
3 5 7 -1 -1 2 4
```

**输出：**
```text
3 7 2
```

### 示例二

**输入：**
```text
5 9 8 -1 -1 7 -1 -1 -1 -1 -1 6
```

**输出：**
```text
5 8 7 6
```

## 解题思路

1. 插入0坐标的值。
2. 计算二叉树的深度`depth`。
3. 计算最后一层首节点的索引`start`。
4. 遍历该层的所有节点，找到值最小的叶子节点。
5. 返回该节点到根节点的所有路径。

## 解题代码

```python
import math


def solve_method(nums):
    nums.insert(0, 0)
    # nums第一个元素无意义，为额外添加元素，目的是对齐下标
    depth = math.ceil(math.log2(len(nums)))
    # 得到最后一层节点的索引
    start = 2 ** (depth - 1)
    min_value, index = math.inf, -1
    # 遍历该层的所有节点
    for i in range(start, len(nums)):
        if nums[i] != -1 and nums[i] < min_value:
            # 取出最小的叶子节点
            min_value, index = nums[i], i
    # 得到该节点的路径
    path = []
    while index > 0:
        path.append(nums[index])
        index = index // 2
    return path[::-1]


if __name__ == '__main__':
    tree_nodes = [3, 5, 7, -1, -1, 2, 4]
    assert solve_method(tree_nodes) == [3, 7, 2]

    tree_nodes = [5, 9, 8, -1, -1, 7, -1, -1, -1, -1, -1, 6]
    assert solve_method(tree_nodes) == [5, 8, 7, 6]
```

