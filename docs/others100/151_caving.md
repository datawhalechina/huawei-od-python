# 151 洞穴探险

## 题目描述

某探险队负责对地下洞穴进行探险，探险队成员在进行探险任务时，随身携带的记录器会不定期的记录自身的坐标。但在记录的间隙也会记录其他数据，探险工作结束后，探险队需要获取到某成员在探险过程中相对于探险队总部最远的足迹位置。

1. 仪器记录坐标时，坐标的数据格式`(x,y)`，如`(1,2)`、`(100,200)`。其中0 < x,y < 1000，同时存在非法坐标，如`(01, 1)`、`(1, 01)`、`(0, 100)`。
2. 设定探险队总部的坐标为`(0,0)`，某位置`(x,y)`相对总部的距离为`x * x + y * y`。
3. 若两个坐标的相对总部距离相同，则第一次到达的坐标为最远的足迹。
4. 若仪器中的坐标都不合法，输出总部坐标`(0,0)`。 
   
**备注：** 不需要考虑双层括号嵌套的情况比如`sfsdfsd((1,2))`

## 输入描述

输入一行字符串，表示记录仪中的数据，如：
```
ferga13fdsf3(100,200)f2r3rfasf(300,400)
```

## 输出描述

输出字符串，表示最远足迹到达的坐标，如：`(300,400)`

## 示例描述

### 示例一

**输入：**

```text
ferg(3,10)a13fdsf3(3,4)f2r3rfasf(5,10)
```

**输出：**

```text
(5,10)
```

**说明：**

记录仪中的合法坐标有三个`(3,10)`、`(3,4)`、`(5,10)`，其中`(5,10)`是相距总部最远的坐标，所以，输出`(5,10)`。

### 示例二

**输入：**

```text
asfefaweawfawf(0,1)fe
```

**输出：**

```text
(0,0)
```

**说明：**

记录仪中的坐标都不合法，输出总部坐标`(0,0)`。

## 解题思路

1. 用正则表达式按照坐标的数据格式取出坐标，存入列表`coordinates`。
2. 将合法的坐标存入列表`valid_coordinates`。
3. 将列表`valid_coordinates`按照相对总部的距离从远到近排序。
4. 返回排序之后的第一个值的坐标（即距离总部最远的坐标）。

## 解题代码

```python
import re


def solve_method(records):
    coordinates = re.findall(r'\((\d+),(\d+)\)', records)
    valid_coordinates = []
    for coordinate in coordinates:
        x, y = map(int, coordinate)
        if 0 < x < 1000 and 0 < y < 1000:
            valid_coordinates.append((x, y))
    if len(valid_coordinates) == 0:
        return "(0,0)"

    valid_coordinates.sort(key=lambda x: x[0] ** 2 + x[1] ** 2, reverse=True)
    return f"({valid_coordinates[0][0]},{valid_coordinates[0][1]})"


if __name__ == '__main__':
    records = "ferg(3,10)a13fdsf3(3,4)f2r3rfasf(5,10)"
    assert solve_method(records) == "(5,10)"

    records = "asfefaweawfawf(0,1)fe"
    assert solve_method(records) == "(0,0)"
```

