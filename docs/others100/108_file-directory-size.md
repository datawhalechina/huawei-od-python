# 108 文件目录大小

## 题目描述

一个文件目录的数据格式：`目录id 本目录中文件大小 (子目录id列表)`。其中目录id全局唯一，取值范围是[1,200]，本目录中文件大小范围是[1,1000]，子目录id列表个数是[0,10]。

例如：
```text
1 20 (2,3)
``` 

表示目录1中的文件总大小是20，有两个子目录，id分别是2和3。

现在输入一个文件系统中所有目录信息，以及待查询的目录id，返回这个目录和及该目录所有子目录的大小之和。

## 输入描述

第一行为两个数字`M`和`N`，分别表示目录的个数和待查询的目录id，取值范围是1 <= M <= 100、1<= N <= 200。

接下来`M`行，每行为1个目录的数据：`目录id 本目录中文件大小 (子目录id列表)`，子目录列表中的子目录id以`,`分隔。

## 输出描述

待查询目录及其子目录的大小之和。

## 补充说明

不用考虑输入数据不合法的情况；假设最多100个输入文件。

## 示例描述

### 示例一

**输入：**

```text
3 1
3 15 ()
1 20 (2)
2 10 (3)
```

**输出：**

```text
45
```

**说明：**  

目录1大小为20，包含一个子目录2（大小为10），子目录2包含一个子目录3（大小为15）。

所以，总的大小为20+10+15=45.

### 示例二

**输入：**

```text
4 2
4 20 ()
5 30 ()
2 10 (4,5)
1 40 ()
```

**输出：**

```text
60
```

**说明**

目录2包含2个子目录4和5，总的大小为10+20+30=60。

## 解题思路

1. 建立一个字典`dir_map`，`key`为目录id，`value`依次存放目录大小、子目录id。
2. 使用深度优先搜索DFS：
    - 确定参数：待查询的目录id `n`、目录字典`dir_map`。
    - 终止条件：当没有子目录时，返回当前目录的大小。
    - 递归处理：判断查询目录id是否在`dir_map`中，如果存在，遍历子目录，并继续递归搜索，把目录大小累加到结果值中。
3. 返回最终结果，即带查询目录的大小。    

## 解题代码

```python
def get_dir_id(string):
    dir_ids = []
    # 除字符串的首尾括号
    trimmed_str = string[1:-1]
    if not trimmed_str:
        return dir_ids
    trimmed_str = trimmed_str.split(",")
    dir_ids = list(map(int, trimmed_str))
    return dir_ids


def dfs(n, dir_map):
    if n in dir_map and len(dir_map[n]) == 1:
        return dir_map[n][0]

    dir_size = 0
    if n in dir_map:
        data = dir_map[n]
        dir_size = data[0]
        for i in range(1, len(data)):
            dir_size += dfs(data[i], dir_map)
    return dir_size


def solve_method(n, dirs):
    dir_map = {}
    for i in range(len(dirs)):
        a, b, c = dirs[i].split()
        dir_id = int(a)
        dir_size = int(b)
        dir_map[dir_id] = [dir_size] + get_dir_id(c)

    dir_total_size = dfs(n, dir_map)
    return dir_total_size


if __name__ == "__main__":
    dirs = ["3 15 ()", "1 20 (2)", "2 10 (3)"]
    assert solve_method(1, dirs) == 45
    dirs = ["4 20 ()", "5 30 ()", "2 10 (4,5)", "1 40 ()"]
    assert solve_method(2, dirs) == 60
```