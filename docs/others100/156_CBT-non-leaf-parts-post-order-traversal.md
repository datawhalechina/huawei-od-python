# 156 完全二叉树非叶子部分后序遍历

## 题目描述

给定一个以顺序储存结构存储整数值的完全二叉树序列（最多1000个整数），请找出此完全二叉树的所有非叶子节点部分，然后采用后序遍历方式将此部分树（不包含叶子）输出。

1. 只有一个节点的树，此节点认定为根节点（非叶子）。
2. 此完全二叉树并非满二叉树，可能存在倒数第二层出现叶子或者无右叶子的情况。

其他说明：二叉树的后序遍历是基于根来说的，遍历顺序为：左-右-根。

## 输入描述

一个通过空格分隔的整数序列字符串。

## 输出描述

非叶子部分树结构的后序遍历结果。

**补充说明：**

输出数字以空格分隔。

## 示例描述

### 示例一

**输入：**
```text
1 2 3 4 5 6 7
```

**输出：**
```text
2 3 1
```

**说明：**  

找到非叶子部分树结构，然后采用后续遍历输出。

## 解题思路

**基本思路：** 使用深度优先搜索DFS求解。

1. 使用深度优先搜索遍历树的所有节点：
    - 确定参数：遍历索引`index`。
    - 终止条件：如果索引超出列表范围，返回空列表。
    - 递归处理：
        - 计算左右子节点的索引。
        - 递归遍历左子树，再递归遍历右子树。
        - 最后遍历根节点：在每次递归调用后，检查当前节点是否是非叶子节点（即至少有一个子节点），如果是，则将其索引添加到结果列表中。
2. 返回结果列表中索引对应的非叶子节点的值。

## 解题代码

```python
def solve_method(nums):
    def post_order_non_leaf(index):
        # 如果索引超出列表范围，返回空列表
        if index >= len(nums):
            return []

        # 计算左右子节点的索引
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        # 后序遍历：先左子树，再右子树，最后根节点
        left_result = post_order_non_leaf(left_child)
        right_result = post_order_non_leaf(right_child)

        # 如果当前节点是非叶子节点，添加到结果中
        if left_child < len(nums) or right_child < len(nums):
            return left_result + right_result + [index]
        return []

    non_leaf_index = post_order_non_leaf(0)
    return [nums[x] for x in non_leaf_index]


if __name__ == "__main__":
    assert solve_method([1, 2, 3, 4, 5, 6, 7]) == [2, 3, 1]
    assert solve_method([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [4, 5, 2, 3, 1]
```