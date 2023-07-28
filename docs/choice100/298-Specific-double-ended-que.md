# 298 特异性双端队列

## 题目描述
有一个特异性的双端队列，该队列可以从头部到尾部添加数据，但是只能从头部移除数据。
小A一次执行 2n 个指令往队列中添加数据和移除数据，
其中 n 个指令是添加数据(可能从头部也可以从尾部添加)
依次添加 1 到 n , n 个指令是移出数据
现在要求移除数据的顺序为 1 到 n ，
为了满足最后输出的要求, 小A可以在任何时候调整队列中的数据的顺序
请问,小A最少需要调整几次才能满足移除数据的顺序正好是 1 到 n
## 输入描述
第一行一个整数 n ，表示数据范围
接下来有 2n 行,其中有 n 行为添加数据:
指令head add x表示从头部添加数据x \
tail add x表示从尾部添加数据x
另外 n 行为移除数据指令,指令为remove形式,表示移除一个数据

$1≤n≤3×10^5$
## 输出描述
一个整数，表示小A要调整的最小次数
### 示例一
**输入：**
```shell
3
head add 1
remove
tail add 2
head add 3
remove
remove
```

**输出：**
```shell
1
```

## 解题思路
本题目标是实现了一个队列的模拟，使用了 Python 的 collections 模块中的 deque 类来实现。主要实现了三种操作 \
1.将数字添加到队列的头部，使用 deque 的 appendleft 方法实现 \
2.将数字添加到队列的尾部，使用 deque 的 append 方法实现。 \
3.将队列的头部数字弹出，使用 deque 的 popleft 方法实现。 \
如果弹出的队列的头部数字不是预期的数字，则对队列进行排序，并且将排序的次数加一。 \
最后，代码返回排序的次数 times。

## 解题代码

```python
# 输入获取
n = int(input())
cmds = [input() for i in range(2 * n)]
 
 
# 算法入口
def getResult(cmds):
    size = 0
    isSorted = True
    count = 0
 
    for cmd in cmds:
        if cmd.startswith("head add"):
            if size > 0 and isSorted:
                isSorted = False
            size += 1
        elif cmd.startswith("tail add"):
            size += 1
        else:
            if size <= 0:
                continue
 
            if not isSorted:
                count += 1
                isSorted = True
 
            size -= 1
 
    return count
 
 
# 算法调用
print(getResult(cmds))
```