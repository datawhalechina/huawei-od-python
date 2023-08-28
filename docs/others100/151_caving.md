# 151 洞穴探险

## 题目描述

某探险队负责对地下洞穴进行探险，探险队成员在进行探险任务时，随身携带的记录器会不定期的记录自身的坐标。但在记录的间隙也会记录其他数据，探险工作结束后，探险队需要获取到某成员在探险过程中相对于探险队总部最远的足迹位置。

1. 仪器记录坐标时，坐标的数据格式（x,y）,如`( 1, 2), (100,200)`

2. 设定探险队总部的坐标为（0，0），某位置（x，y）相对总部的距离为`x*x+y*y`

3. 若两个坐标的相对总部距离相同，则第一次到达的坐标为最远的足迹

4. 若仪器中的坐标都不合法输出总部坐标（0，0）

   备注：不需要考虑双层括号嵌套的情况比如`sfsdfsd((1,2))`

## 输入描述

字符串表示记录仪中的数据如：
```
ferga13fdsf3(100,200)f2r3rfasf(300,400)
```
## 输出描述

字符串表示最远足迹到达的坐标如：

```
（300，400）
```



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

## 解题思路

首先使用正则表达式从输入数据中提取所有的坐标，并进行合法性判断。然后计算每个坐标相对于总部的距离，并找到距离最大的坐标。最后返回最远足迹到达的坐标。如果输入数据中没有合法的坐标，则返回总部坐标(0,0)。

## 解题代码

```python
import re


def get_farthest_coordinate(data):
    coordinates = re.findall(r'\((\d+),(\d+)\)', data)
    valid_coordinates = []
    for coordinate in coordinates:
        x, y = map(int, coordinate)
        if 0 < x < 1000 and 0 < y < 1000:
            valid_coordinates.append((x, y))
    if len(valid_coordinates) == 0:
        return "(0,0)"

    distances = [x ** 2 + y ** 2 for x, y in valid_coordinates]
    max_distance_index = distances.index(max(distances))
    return f"({valid_coordinates[max_distance_index][0]},{valid_coordinates[max_distance_index][1]})"


data = input()
result = get_farthest_coordinate(data)
print(result)
```

