# 304 箱子之字形摆放

## 题目描述
有一批箱子（形式为字符串，设为str），

要求将这批箱子按从上到下以之字形的顺序摆放在宽度为 n 的空地，请输出箱子的摆放位置。

例如：箱子ABCDEFG，空地宽度为3，摆放结果如图：

![](https://raw.githubusercontent.com/jackielics/image-hosting-service/main/2023-07-23_11-23-17.png?token=GHSAT0AAAAAACE7ANKIUWXY2OOHY4GVOQZMZF4TWNA)

​则输出结果为：

AFG

BE

CD

## 输入描述
输入一行字符串，通过空格分隔，前面部分为字母或数字组成的字符串str，表示箱子；

后面部分为数字n，表示空地的宽度。例如：

ABCDEFG 3

备注：

1. 请不要再最后一行输出额外的空行
2. str只包含字母和数字，1 <= len(str) <= 1000
3. 1 <= n <= 1000

## 输出描述
箱子摆放结果，如题目示例所示

### 示例一
**输入：**
```shell
ABCDEFG 3
```

**输出：**
```shell
AFG
BE
CD
```

**说明：**  
1. 请不要再最后一行输出额外的空行
2.  str 只包含字母和数字，1 <= Len(str) <= 1000
3.  1 <= n <= 1000

## 解题思路
- 在 solve_method()函数中，通过使用 split() 函数分字符串 line，可以得到需要输出的字符 str 和每行的字符数n。
- 将 str 转换为字符列表 chars

## 解题代码

```python
import re
 
# 如果端口组间存在2个及以上不同端口相同，则认为这2个端口组互相关联，可以合并。
# 下面方法实现中：要形成两对“端口值不同的端口对”，即 a = [1,2,3]，b=[2,3,4]可以合并，但是a = [1,3,3]，b=[3,3,4]不可以合并
def canUnion(port1, port2):
    set1 = set(port1)
    set2 = set(port2)
 
    same = 0
    for v in set1:
        if v in set2:
            same += 1
            if same >= 2:
                return True
 
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
 
    # return list(map(distinctAndSort, ports))
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