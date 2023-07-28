# 303 端口合并

## 题目描述
有M(1<=M<=10)个端口组，
每个端口组是长度为N(1<=N<=100)的整数数组，
如果端口组间存在2个及以上不同端口相同，
则认为这2个端口组互相关联，可以合并
第一行输入端口组个数M，再输入M行，每行逗号分隔，代表端口组。
输出合并后的端口组，用二维数组表示

## 输入描述
第一行输入一个数字M \
第二行开始输入M行，每行是长度为N的整数数组，用逗号分割

## 输出描述
合并后的二维数组

### 示例一
**输入：**
```shell
4
4
2,3,2
1,2
5
```

**输出：**
```shell
[[4],[2,3],[1,2],[5]]
```

**说明：**  
仅有一个端口2相同，不可以合并

### 示例二
**输入：**
```shell
3
2,3,1
4,3,2
5
```

**输出：**
```shell
[[1,2,3,4],[5]]
```

**说明：**  
### 示例三
**输入：**
```shell
6
10
4,2,1
9
3,6,9,2
6,3,4
8
```

**输出：**
```shell
[[10],[1,2,3,4,6,9],[9],[8]]
```

**说明：**  
## 解题思路
算法思想:
- 输入自行车限重 m 和部门人数 n。
- 输入每个人的体重，并将体重排序。
- 设置双指针 i和j，分别指向最小和最大体重的人。
- 如果两人体重之和小于等于 m，则租一辆双人自行车。如果两人体重之和大于 m，则租一辆单人自行车.
- 最后输出最少需要的自行车数量。

## 解题代码

```python
import re
 
# 如果端口组间存在2个及以上不同端口相同，则认为这2个端口组互相关联，可以合并。
# 下面方法实现中：对于“不同端口”的理解是：端口位置不同，端口值可以相同，即以不同位置的端口视为不同端口
def canUnion(port1, port2):
    port1.sort()
    port2.sort()
 
    same = 0
    i = 0
    j = 0
 
    while i < len(port1) and j < len(port2):
        if port1[i] == port2[j]:
            i += 1
            j += 1
            same += 1
            if same >= 2:
                return True
        elif port1[i] > port2[j]:
            j += 1
        else:
            i += 1
 
    return False
 
 
# 从头开始尝试合并端口组
def forPorts(ports):
    # 这里倒序遍历端口组是为了实现：组外顺序保持输入顺序
    for i in range(len(ports) - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            # 判断两个端口是否可以合并
            if canUnion(ports[i], ports[j]):
                # 将后面的端口组，并入前面的端口组，这样就不会破坏组外顺序
                ports[j].extend(ports[i])
                ports.pop(i)
                return True  # 继续尝试合并
 
    return False  # 合并尝试结束
 
 
# 组内相同端口仅保留一个，从小到达排序
def distinctAndSort(port):
    tmp = list(set(port))
    tmp.sort()
    return tmp
 
 
# 算法入口
def getResult(ports):
    while True:
        if not forPorts(ports):
            break
 
    # return list(map(distinctAndSort, ports)) # 如果输出内容不去除空格，可得83.33%通过率
    return re.sub(f"\\s", "", str(list(map(distinctAndSort, ports))))
 
 
# 输入获取
m = int(input())
 
if m < 1 or m > 10:
    print("[[]]")
else:
    ports = [list(map(int, input().split(","))) for _ in range(m)]
    if len(list(filter(lambda p: len(p) < 1 or len(p) > 100, ports))) > 0:
        print("[[]]")
    else:
        print(getResult(ports))
```