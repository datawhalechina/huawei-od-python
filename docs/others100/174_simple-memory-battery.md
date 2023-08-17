# 174 简易内存池

## 题目描述

请实现一个简易内存池，根据请求命令完成内存分配和释放。

内存池支持两种操作命令，`REQUEST`和`RELEASE`，其格式为：

1. `REQUEST=请求的内存大小` 表示请求分配指定大小内存
   - 如果分配成功，返回分配到的内存首地址。
   - 如果内存不足，或指定的大小为零，则输出`error`。
2. `RELEASE=释放的内存首地址`表示释放掉之前分配的内存
   - 释放成功无需输出。
   - 如果释放不存在的首地址，则输出`error`。

**注意：**

1. 内存池总大小为100字节。
2. 内存池地址分配必须是连续内存，并优先从低地址分配。
3. 内存释放后可被再次分配，已释放的内存在空闲时不能被二次释放。
4. 不会释放已申请的内存块的中间地址。
5. 释放操作只是针对首地址所对应的单个内存块进行操作，不会影响其他内存块。

## 输入描述

首行为整数`N`，表示操作命令的个数，取值范围是0 < N <= 100。

接下来的`N`行，每行将给出一个操作命令，操作命令和参数之间用`=`分割，输出见题目输出要求。

## 输出描述

释放成功无需输出，如果释放不存在的首地址，则输出`error`。

## 示例描述

### 示例一

**输入：**

```text
2
REQUEST=10
REQUEST=20
```

**输出：**

```text
0
10
```

### 示例二

**输入：**

```text
5
REQUEST=10
REQUEST=20
RELEASE=0
REQUEST=20
REQUEST=10
```

**输出：**

```text
0
10
30
0
```

**说明：**

- 第1条指令，申请地址0\~9的10个字节内存，返回首地址0。
- 第2条指令，申请地址10\~29的20字节内存，返回首地址10。
- 第3条指令，释放首地址为0的内存申请，0\~9地址内存被释放，变为空闲，释放成功，无需输出。
- 第4条指令，申请20字节内存，0\~9地址内存连续空间不足20字节往后查找到30\~49地址返回首地址30。
- 第5条指令，申请地址10字节，0~9地址内存连续空间足够，返回首地址0。

## 解题思路

**基本思路：**

1. 创建一个`MemoryPool`内存池类，存储剩余内存区间和已经分配的内存区间，每个元素是一个二元组，表示始末地址。
2. 实现申请和释放操作：
   - 进行申请操作时，寻找合适的内存空间，如果找到，则存入已分配内存区间，如果该区间较大，则将剩余切分完的区间再存入剩余的内存区间。
   - 进行释放操作时，恢复剩余内存区间，删除已分配内存区间，对区间进行合并。
3. 遍历所有的操作命令：
   - 当进行申请操作时，每一次请求的初始内存地址需要返回，存入结果列表中。
   - 当进行释放操作时，执行正确无需返回，执行错误会返回`error`，存入结果列表中。
4. 返回结果列表。   

## 解题代码

```python
class MemoryPool:
    def __init__(self):
        # 存储剩余的内存区间，每个元素是一个二元组，表示始末地址
        self.free_list = [(0, 99)]
        # 存储已经分配的内存区间
        self.memory = []

    def request(self, size):
        if size == 0:
            return "error"
        # 遍历整个可以选取的内存区间
        for i, (start, end) in enumerate(self.free_list):
            if end - start + 1 >= size:
                # 将合适的区间取出来，原列表内则删除掉
                self.free_list.pop(i)
                # 存放入已经分配的内存区间
                self.memory.append((start, start + size - 1))

                # 如果该区间较大，分配完还有多余的空间
                # 则将剩余切分完的区间再存入剩余的内存区间
                if end - start + 1 > size:
                    self.free_list.insert(i, (start + size, end))
                return start
        return "error"

    def release(self, start):
        # 先找已分配的内存的首地址，是否有与start匹配的
        for ind, (_start, _end) in enumerate(self.memory):
            # 找到该区间后，从分配的memory中去掉，添加到未分配区间free_list中
            if _start == start:
                self.free_list.append(self.memory.pop(ind))

                # 区间之间有交集，我们要合并区间
                stack = []
                # 对空闲区间按照首地址进行排序
                self.free_list.sort()

                for interval in self.free_list:
                    if stack and stack[-1][1] == interval[0]:
                        # 如果尾地址与当前首地址相同时，则合并区间
                        stack[-1][1] = interval[1]
                    stack.append(interval)
                # 合并完成
                self.free_list = stack
                return None
        return "error"


def solve_method(n, dis):
    result = []
    mp = MemoryPool()
    for i in range(n):
        cmd = dis[i].split('=')
        if cmd[0] == 'REQUEST':
            # 每一次请求的初始内存地址需要返回
            ans1 = mp.request(int(cmd[1]))
            result.append(ans1)
        else:
            ans2 = mp.release(int(cmd[1]))
            # 执行正确返回None，即无返回值，执行错误会返回error
            if ans2:
                result.append(ans2)
    return result


if __name__ == '__main__':
    assert solve_method(5, ['REQUEST=10', 'REQUEST=20', 'RELEASE=0', 'REQUEST=20', 'REQUEST=10']) == [0, 10, 30, 0]
    assert solve_method(2, ['REQUEST=10', 'REQUEST=20']) == [0, 10]
    assert solve_method(4, ['REQUEST=20', 'REQUEST=30', 'REQUEST=50', 'REQUEST=10']) == [0, 20, 50, 'error']
    assert solve_method(4, ['REQUEST=10', 'REQUEST=20', 'RELEASE=0', 'RELEASE=0']) == [0, 10, 'error']

```



