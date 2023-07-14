# 281 打印文件

## 题目描述

有5台打印机打印文件，每台打印机有自己的待打印队列。因为打印的文件内容有轻重缓急之分，所以队列中的文件有1-10不同的优先级，其中数字越大优先级越高。打印机会从自己的待打印队列中选择优先级最高的文件来打印。如果存在两个优先级一样的文件，则选择最早进入队列的那个文件。

现在请你来模拟这5台打印机的打印过程。

## 输入描述

每个输入包含1个测试用例，每个测试用例第1行给出发生事件的数量。

接下来有`N`行（0 < N < 1000），分别表示发生的事件。共有如下两种事件：
1. `IN P NUM`，表示有一个拥有优先级`NUM`的文件放到了打印机`P`的待打印队列中。（0 < P <= 5, 0 < NUM <= 10）;
2. `OUT P`，表示打印机`P`进行了一次文件打印，同时该文件从待打印队列中取出。（0 < P <= 5）。

## 输出描述

对于每个测试用例，每次`OUT P`事件，请在一行中输出文件的编号。如果此时没有文件可以打印，请输出`NULL`。

文件的编号定义为：`IN P NUM`事件发生第`X`次，此处待打印文件的编号为`X`，编号从1开始。

## 示例描述

### 示例一

**输入：**
```
7
IN 1 1
IN 1 2
IN 1 3
IN 2 1
OUT 1
OUT 2
OUT 2
```

**输出：**
```
3
4
NULL
```

### 示例一

**输入：**
```
5
IN 1 1
IN 1 3
IN 1 1
IN 2 3
OUT 1
```

**输出：**
```
2
```

## 解题思路

1. 本题构建多个优先序列，用于表示待打印队列。
2. 构造一个打印机序列，其中key是打印机编号，value是待打印的优先序列。
3. 分别处理`IN P NUM`和`OUT P`指令：
    - `IN P NUM`指令：使用优先队列，由于优先序列是越小越优先，所以`num`要取负号，将待打印文件编号放入优先队列中。
    - `OUT P`指令：从优先队列中取出文件编号，放入结果队列中。
4. 返回结果队列。    

## 解题代码

```python
import heapq

def solve_method(print_list):
    result = []
    file_id = 1
    # 构造一个打印机序列，其中key是打印机编号，value是待打印的优先序列
    printers = {}
    for command in print_list:
        commands = command.split()
        if commands[0] == "IN":
            p = commands[1]
            num = int(commands[2])
            if p not in printers:
                printers[p] = []
            # 使用优先队列，由于优先序列是越小越优先，所以num要取负号
            heapq.heappush(printers[p], (-num, file_id))
            file_id += 1
        elif commands[0] == "OUT":
            p = commands[1]
            if p in printers and len(printers[p]) > 0:
                # 从优先队列中取出文件编号
                _, file_id = heapq.heappop(printers[p])
                result.append(file_id)
            else:
                result.append("NULL")

    return result
```