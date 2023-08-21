# 052 报文响应时间

## 题目描述

IGMP协议中，有一个字段称作最大响应时间（MaxResponseTime），HOST收到查询报文，解析出MaxResponseTime字段后，需 要在（0，MaxResponseTime］（s）时间内选取随机时间回应一个响应报文，如果在随机时间内收到一个新的查询报文，则会根据两者时间的大小，选取小的一方刷新回应时间。

最大响应时间有如下计算方式：

当 `MaxRespCode` ＜128， `MaxRespTime` ＝ `MaxRespCode`；

当 `MaxRespCode` ＞＝128，`MaxRespTime ＝（mant ｜0x10）＜＜（exp＋3）`； 
`|0| 123|4567 |`

`|1|exp | mant|`

注：exp最大响应时间的高5～7位；mant为最大响应时间的低4位。

其中接收到的`MaxRespCode` 最大值为255，以上出现所有字段均为无符号数。现在我们认为HOST接收到查询报文时，选取的随机时间必定为最大值。

现给出HOST收到查询报文个数C，HOST收到报文的时间＄TS，以及查询报文的最大响应时间字段值M，请计算出HOST发送响应报文的时间。

## 输入
第一行为查询报文个数C，后续每行分别为HOST收到报文时间T，及最大响应字段M，以空格分割

## 输出描述
HOST发送响应报文的时间

### 示例一

**输入：**
```text
3
0 20
1 10
8 20
```

**输出描述：**
```text
11
```

### 示例二

**输入：**

```text
2
0 255
200 60
```

**输出：**
```text
260
```
**编码思路**

这个题目需要对一系列的字符串进行判断，分别对应三个情况：

·缺勤超过1次

1．没有连续的迟到／早退

2．任意连续7次考勤缺勤／迟到／早退不超过3次

针对每个字符串列表，依次进行上述三个判断，判断过程中注意细节问题，如判断缺勤次数需要使用count函数，判断连续缺勤或迟到／ 早退需要使用zip函数等。

**核心知识点**
1. 列表（list）的基本操作，如创建、遍历、添加、删除等 
2. 列表推导式和生成器表达式的使用
3. 字符串（str）的基本操作，如切片、拼接、查找、替换等 
4. 迭代器（iterator）和生成器（generator）的概念及使用 
5. zip 函数和count 函数的使用


## 解题代码

```python
def solve_method(days):
    res = []  # 初始化结果列表
    for day in days:  # 遍历每一天的状态
        absent = day.count("absent")  # 计算 "absent" 的数量
        # 检查是否有超过1个 "absent" 或连续的 "late" 或 "leaveearly"
        if absent > 1 or any(
                cur in ("late", "leaveearly") and next in ("late", "leaveearly") for cur, next in zip(day, day[1:])):
            res.append("false")  # 如果满足条件，则添加 "false" 到结果列表
            continue
        # 将每天的状态转换为整数列表，其中 "present" 转换为0，其他状态转换为1
        ints = [1 if item != "present" else 0 for item in day]
        # 检查整数列表的长度是否小于或等于7，并且总和是否大于或等于3
        if len(ints) <= 7 and sum(ints) >= 3:
            res.append("false")  # 如果满足条件，则添加 "false" 到结果列表
        else:
            # 检查任何连续的7天是否有3天或更多的非 "present" 状态
            flag = any(sum(ints[i:i + 7]) >= 3 for i in range(len(ints) - 7))
            res.append(str(not flag).lower())  # 添加结果到结果列表
    print("".join(res))  # 打印结果列表

if __name__ == "__main__":
    n = int(input())  # 读取天数
    days = [input().split() for _ in range(n)]  # 读取每一天的状态
    solve_method(days)  # 调用解决方法

```

