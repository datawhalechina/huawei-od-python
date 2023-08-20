# 051 员工出勤

## 题目描述

公司用一个字符串来标识员工的出勤信息 

1. `absent`：缺勤
2. `late`：迟到 
3. `leaveearly`：早退 
4. `present`：正常上班

现需根据员工出勤信息，判断本次是否能获得出勤奖， 能获得出勤奖的条件如下：

1．缺勤不超过`1`次

2．没有连续的迟到／早退

3．任意连续`7`次考勤，缺勤／迟到／早退，不超过`3`次

## 输入
`用户的考勤数据字符串记录条数＞＝1`
`输入字符串长度＜10000;`
不存在非法输入 如：
`2`
`present`

`present absent present present leaveearly present absent`
## 输出描述
根据考勤数据字符串

如果能得到考勤奖输出 `true` 否则输出 `false` `true false`
### 示例一

**输入：**
```text
present present
```

**输出描述：**
```text
true true
```

### 示例二

**输入：**

```text
2
present
present absent present present leaveearly present absent
```

**输出：**
```text
true false
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

