# 312 静态扫描最优成本

## 题目描述

静态扫描快速识别源代码的缺陷，静态扫描的结果以扫描报告作为输出：

1. 文件扫描的成本和文件大小相关，如果文件大小为`N` ，则扫描成本为`N`个金币。  
2. 扫描报告的缓存成本和文件大小无关，每缓存一个报告需要`M`个金币。
3. 扫描报告缓存后，后继再碰到该文件则不需要扫描成本，直接获取缓存结果。

给出源代码文件标识序列和文件大小序列，求解采用合理的缓存策略，最少需要的金币数。

## 输入描述

第一行是缓存一个报告金币数`M`，取值范围是$1 \leqslant M \leqslant 100$。  

第二行是文件标识序列：取值范围是$F_1,F_2,F_3,\cdots,F_N$，其中 $1 \leqslant N \leqslant 10000,1 \leqslant F_i \leqslant 1000$。  

第三行是文件大小序列：取值范围是$S_1,S_2,S_3,\cdots,S_N$，其中 $1 \leqslant N \leqslant 10000,1 \leqslant S_i \leqslant 10$。 

## 输出描述

采用合理的缓存策略，需要的最少金币数。

## 示例描述

### 示例一

**输入：**
```text
5
1 2 2 1 2 3 4
1 1 1 1 1 1 1
```

**输出：**
```text
7
```

**说明：**

文件大小相同，扫描成本均为1个金币。缓存任意文件均不合算，因而最少成本为7金币。

### 示例二

**输入：**
```text
5
2 2 2 2 2 5 2 2 2
3 3 3 3 3 1 3 3 3
```

**输出：**
```text
9
```

**说明：**  

2号文件出现了8次，扫描加缓存成本共计3+5=8，不缓存成本为3*8=24，显然缓存更优，最优成本为8+1=9。

## 解题思路

1. 初始化文件出现次数字典`count`，`key`为文件标识，`value`为文件出现次数。
2. 初始化文件大小`size`，`key`为文件标识，`value`为文件大小。
3. 遍历文件出现次数：
    - 计算每次都重新扫描的成本`rescan_amount`。
    - 计算扫描一次+缓存的成本`cached_amount`。
    - 得到两者最小值，然后累加，存入结果值。
4. 返回结果值。   

## 解题代码

```python
from collections import defaultdict


def solve_method(m, file_ids, file_sizes):
    # count用于保存每个文件出现的次数
    count = defaultdict(int)
    # size用于保存文件的大小，即扫描成本
    size = {}

    for i in range(len(file_ids)):
        file_id = file_ids[i]
        count[file_id] += 1

        if size.get(file_id) is None:
            size[file_id] = file_sizes[i]

    result = 0
    for file_id in count.keys():
        # 每次都重新扫描的成本
        rescan_amount = count[file_id] * size[file_id]
        # 扫描一次+缓存的成本
        cached_amount = size[file_id] + m
        result += min(rescan_amount, cached_amount)
    return result


if __name__ == '__main__':
    file_ids = [1, 2, 2, 1, 2, 3, 4]
    file_sizes = [1, 1, 1, 1, 1, 1, 1]
    assert solve_method(5, file_ids, file_sizes) == 7

    file_ids = [2, 2, 2, 2, 2, 5, 2, 2, 2]
    file_sizes = [3, 3, 3, 3, 3, 1, 3, 3, 3]
    assert solve_method(5, file_ids, file_sizes) == 9
```