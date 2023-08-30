# 051 员工出勤

## 题目描述

公司用一个字符串来标识员工的出勤信息： 

- `absent`：缺勤。
- `late`：迟到。 
- `leaveearly`：早退。 
- `present`：正常上班。

现需根据员工出勤信息，判断本次是否能获得出勤奖，能获得出勤奖的条件如下：
- 缺勤不超过1次。
- 没有连续的迟到、早退。
- 任意连续7次考勤，缺勤、迟到、早退，不超过3次。

## 输入描述

第一行输入员工的考勤数据字符串记录条数`N`，取值范围是记录条数大于等于1。

从第2行开始到第`N+1`行，输入员工的考勤信息，用空格分隔，输入字符串长度小于10000，不存在非法输入。

## 输出描述

根据考勤数据字符串，如果能得到考勤奖输出`true`，否则输出`false`。

## 示例描述

### 示例一

**输入：**
```text
2
present
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

## 解题思路

1. 遍历每一条员工的出勤记录：
    - 使用`count`计算缺勤次数，如果超过1次，没有出勤奖。
    - 使用前指针方法，比较当前指针指向的元素，如果有连续的迟到、早退，没有出勤奖。
    - 使用滑动窗口（窗口大小为7），检查任何连续的7天是否有4天或更多的正常上班状态。
2. 返回每一条出勤记录对应的结果。    

## 解题代码

```python
def solve_method(records):
    result = []
    for record in records:
        # 缺勤如果超过1次，没有出勤奖
        if record.count("absent") > 1:
            result.append("false")
            continue

        # 如果有连续的迟到、早退，没有出勤奖
        prev = record[0]
        for day in records[1:]:
            if prev in ["late", "leaveearly"] and day in ["late", "leaveearly"]:
                result.append("false")
                continue

        if len(record) <= 3:
            result.append("true")
        else:
            # 检查任何连续的7天是否有4天或更多的正常上班状态
            flag = all([record[i:i + 7].count("present") >= 4 for i in range(len(record) - 6)])
            result.append(str(flag).lower())

    return result


if __name__ == "__main__":
    records = [["present"],
               ["present", "present"]]
    assert solve_method(records) == ["true", "true"]

    records = [["present"],
               ["present", "absent", "present", "present", "leaveearly", "present", "absent"]]
    assert solve_method(records) == ["true", "false"]

    records = [["present"],
               ["present", "present", "late", "present", "leaveearly", "present", "leaveearly", "present", "late",
                "present"]]
    assert solve_method(records) == ["true", "false"]
```

