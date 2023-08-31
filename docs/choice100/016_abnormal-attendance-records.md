# 016 异常的打卡记录

## 题目描述

考勤记录是分析和考核职工工作时间利用情况的原始依据，也是计算职工工资的原始依据，为了正确地计算职工工资和监督工资基金使用情况，公司决定对员工的手机打卡记录进行异常排查。

如果出现以下两种情况，则认为打卡异常：
1. 实际设备号与注册设备号不一样；
2. 同一个员工的两个打卡记录的时间小于60分钟并且打卡距离超过5km。

给定打卡记录的字符串数组`clockRecords`（每个打卡记录组成为：工号、时间（分钟）、打卡距离（km）、实际设备号、注册设备号），返回其中异常的打卡记录（按输入顺序输出）。

## 输入描述

第一行输入为`N`，表示打卡记录数；之后的`N`行表示打卡记录，每一行表示一条打卡记录。

例如：
```text
2
100000,10,1,ABCD,ABCD
100000,50,10,ABCD,ABCD
```

## 输出描述

输出为异常的打卡记录，例如：
```text
100000,10,1,ABCD,ABCD;100000,50,10,ABCD,ABCD
```

## 备注

1. `clockRecords`长度 <= 1000
2. `clockRecords[i]`格式：`{id},{time},{distance},{actualDeviceNumber},{registeredDeviceNumber}`
3. `id`由6位数字组成
4. `time`由整数组成，范围为0\~1000
5. `distance`由整数组成，范围为0\~100
6. `actualDeviceNumber`和`registeredDeviceNumber`由4位大写字母组成

## 示例描述

### 示例一

**输入：**
```text
2
100000,10,1,ABCD,ABCD
100000,50,10,ABCD,ABCD
```

**输出：**
```text
100000,10,1,ABCD,ABCD;100000,50,10,ABCD,ABCD
```

**说明：**  
第一条记录是异常的，因为第二条记录与它的间隔不超过60分钟，但是打卡距离超过了5km，同理第二条记录也是异常的。

### 示例二

**输入：**
```text
2
100000,10,1,ABCD,ABCD
100000,80,10,ABCE,ABCD
```

**输出：**
```text
100000,80,10,ABCE,ABCD
```

**说明：**  
第二条记录的注册设备号与打卡设备号不一致，所以是异常记录。

### 示例三

**输入：**
```text
2
100000,10,1,ABCD,ABCD
100000,80,10,ABCE,ABCE
```

**输出：**
```text
null
```

**说明：**  
无异常打卡记录，所以返回`null`

## 解题思路

1. 用对象`EmployeeRecord`存储打卡记录，并先判断实际设备号与注册设备号是否一致。
2. 将打卡记录存储在对象列表中
3. 遍历打卡记录的列表：
    - 计算打卡时间
    - 计算打卡距离
    - 如果两个打卡记录时间小于60，并且打卡距离超过5km，打卡异常，设置`vaild`为`False`
4. 得到打卡异常的记录并返回字符串。

## 解题代码

```python
def solve_method(clock_records):
    employee_records = []
    for record in clock_records:
        employee_record = EmployeeRecord(record[0], record[1], record[2], record[3], record[4])
        employee_record.set_vaild(employee_record.check_device_number())
        employee_records.append(employee_record)

    for i in range(len(employee_records)):
        for j in range(i + 1, len(employee_records)):
            if employee_records[i].id == employee_records[j].id:
                # 计算打卡时间
                time_diff = abs(employee_records[i].time - employee_records[j].time)
                # 计算打卡距离
                distance_diff = abs(employee_records[i].distance - employee_records[j].distance)
                # 如果两个打卡记录时间小于60，并且打卡距离超过5km，打卡异常
                if time_diff < 60 and distance_diff > 5:
                    employee_records[i].vaild = False
                    employee_records[j].vaild = False

    # 得到打卡异常的记录
    result = ";".join(str(record) for record in employee_records if not record.vaild)
    return "null" if len(result) == 0 else result


class EmployeeRecord:
    def __init__(self, id, time, distance, actual_device_number, registered_device_number):
        self.id = id
        self.time = time
        self.distance = distance
        self.actual_device_number = actual_device_number
        self.registered_device_number = registered_device_number
        # 打卡是否合法
        self.vaild = True

    def set_vaild(self, vaild):
        self.vaild = vaild

    def __str__(self):
        return f"{self.id},{self.time},{self.distance},{self.actual_device_number},{self.registered_device_number}"

    def check_device_number(self):
        # 实际设备号与注册设备号不一致，打卡异常
        if self.actual_device_number == self.registered_device_number:
            return True
        return False



if __name__ == '__main__':
    clockRecords = [
        ["100000", 10, 1, "ABCD", "ABCD"],
        ["100000", 50, 10, "ABCD", "ABCD"]
    ]
    assert solve_method(clockRecords) == "100000,10,1,ABCD,ABCD;100000,50,10,ABCD,ABCD"

    clockRecords = [
        ["100000", 10, 1, "ABCD", "ABCD"],
        ["100000", 80, 10, "ABCE", "ABCD"]
    ]
    assert solve_method(clockRecords) == "100000,80,10,ABCE,ABCD"

    clockRecords = [
        ["100000", 10, 1, "ABCD", "ABCD"],
        ["100000", 80, 10, "ABCE", "ABCE"]
    ]
    assert solve_method(clockRecords) == "null"
```