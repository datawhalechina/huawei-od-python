#  115 最优调度策略

## 题目描述

在通信系统中有一个常见的问题是对用户进行不同策略的调度，会得到不同系统消耗的性能。假设由`N`个待串行用户，每个用户可以使用`A/B/C`三种不同的调度策略。不同的策略会消耗不同的系统资源，相邻的用户不使用相同的调度策略，根据以上规则进行用户调度，要求返回对系统资源消耗最少的策略。

**例如：**  
第一个用户使用`A`策略，则第二个用户只能使用`B`和`C`策略。对单的用户而言，不同的调度策略对系统资源的消耗可以抽象为数值。

**例如：**  
某用户分别使用`ABC`策略的系统消耗，分别为`15 8 17`，每个用户依次根据当前所能选择的对系统资源消耗最少的策略，保证局部最优，如果有多个满足要求的策略，选最后一个。

## 输入描述

第一行表示用户个数`N`。

接下来表示每一行表示一个用户分别使用三个策略的资源消耗：`resA resB resC`。

## 输出描述

最优策略组合下的总的系统消耗资源数。

## 示例描述

### 示例一

**输入：**

```text
3
15 8 17
12 20 9
11 7 5
```

**输出：**

```text
24
```

**说明：**  

- 1号用户使用`B`策略。
- 2号用户使用`C`策略。
- 3号用户使用`B`策略。
系统资源消耗为8+9+7=24。

## 解题思路

1. 遍历第一个用户的策略：
   - 初始化当前资源消耗
   - 创建前一个用户策略的索引`preIndex`，初始化为第一个用户的调度策略，
   - 遍历后续用户：
      - 根据上一个策略索引，则在`preIndex`标记以外的策略中寻找资源消耗最小值。
      - 将策略对应的资源进行累加，存入当前资源消耗。
   - 获取最小的资源消耗。
3. 返回最小的资源消耗。

## 解题代码

```python
import math


def solve_method(resources):
    min_res = math.inf
    for r in resources[0]:
        # 遍历第一个用户的策略
        total_resource = r
        preIndex = resources[0].index(r)
        for i in range(1, len(resources)):
            resource = resources[i]
            # 从除了preIndex标记以外的策略中选择对系统资源消耗最小的策略
            min_resource = min(resource[:preIndex] + resource[preIndex + 1:])
            preIndex = resource.index(min_resource)
            total_resource += min_resource
        min_res = min(min_res, total_resource)

    return min_res


if __name__ == '__main__':
    resources = [[15, 8, 17],
                 [12, 20, 9],
                 [11, 7, 5]]
    assert solve_method(resources) == 24
```





