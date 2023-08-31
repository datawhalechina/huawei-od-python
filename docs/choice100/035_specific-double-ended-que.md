# 035 特异性双端队列

## 题目描述

有一个特异性的双端队列，该队列可以从头部到尾部添加数据，但是只能从头部移除数据。

小A一次执行`2n`个指令往队列中添加数据和移除数据，其中`n`个指令是添加数据（可能从头部也可以从尾部添加），之后依次添加1到`n`，`n`个指令是移出数据。

现在要求移除数据的顺序为1到`n`，为了满足最后输出的要求，小A可以在任何时候调整队列中的数据的顺序。

请问小A最少需要调整几次才能满足移除数据的顺序正好是1到`n`。

## 输入描述

第一行是一个整数`n`，表示数据范围，接下来有`2n`行，其中有`n`行是添加数据，指令如下：
- 指令`head add x`表示从头部添加数据`x`。
- 指令`tail add x`表示从尾部添加数据`x`。

另外`n`行是移除数据指令，指令为`remove`形式，表示移除一个数据。

`n`的取值范围是1 <= n <= 3 * 10^5

## 输出描述

一个整数，表示小A要调整的最小次数

### 示例一

**输入：**

```text
3
head add 1
remove
tail add 2
head add 3
remove
remove
```

**输出：**
```text
1
```

## 解题思路

1. 标识当前是否输出的顺序正确，记为`isSorted`。
2. 遍历所有的指令：
    - 如果指令是`head add x`，则表示从头部添加，导致输出顺序不正常，设置标识为`False`。
    - 如果指令是`tail add x`，则表示从尾部添加，输出顺序正常。
    - 如果指令是`remove`，如果标识为`False`，则调整次数加1。
3. 返回调整次数。    

## 解题代码

```python
def solve_method(cmds):
    size = 0
    # 标识当前是否输出的顺序正确
    isSorted = True
    count = 0

    for cmd in cmds:
        if cmd.startswith("head add"):
            # 从头部添加，导致输出顺序不正常，设置标识为False
            if size > 0 and isSorted:
                isSorted = False
            size += 1
        elif cmd.startswith("tail add"):
            size += 1
        else:
            if size <= 0:
                continue

            if not isSorted:
                # 如果标识为False，则调整次数加1
                count += 1
                isSorted = True

            # 队列长度减1
            size -= 1

    return count


if __name__ == '__main__':
    cmds = ["head add 1",
            "remove",
            "tail add 2",
            "head add 3",
            "remove",
            "remove"]
    assert solve_method(cmds) == 1
```