# 010-不等式

## 题目描述

给定一组不等式，判断是否成立并输出不等式的最大差（输出浮点数的整数部分）
要求：

1. 不等式系数为double类型，是一个二维数组
2. 不等式的变量为int类型，是一维数组
3. 不等式的目标值为double类型，是一维数组
4. 不等式约束为字符串数组，只能是大于，大于等于，小于，小于等于，等于

例如：不等式组： 

a11 * x1+a12 * x2+a13 * x3+a14 * X4+a15 * x5<=b1; 

a21 * x1+a22 * x2+a23 * x3+a24 * X4+a25 * x5<=b2; 

a31 * x1+a32 * x2+a33 * x3+a34 * X4+a35 * x5<=b3;

```
最大差=max{
(a11*x1+a12*x2+a13*x3+a14*x4+a15*x5-b1),
(a21*x1+a22*x2+a23*x3+a24*x4+a25*x5-b2),
(a31*x1+a32*x2+a33*x3+a34*X4+a35*x5-b3)
},
```

类型为整数（输出浮点数的整数部分）

## 输入描述

1. 不等式组系数（double类型）
   a21,a22,a23,a24,a25
   a31,a32,a33,a34,a35
2. 不等式变量(int类型)
   X1,X2,X3,X4,X5
3. 不等式目标值(double类型)
   <=,<=,<=
   输入：
   a11,a12,a13,a14,a15;
   a21,a22,a23,a24,a25; 
   a31,a32,a33,a34,a35; 
   X1,X2,X3,X4,X5; 
   b1,b2,b3; 
   <=,<=,<=

## 输出描述

## 示例描述

### 示例一

**输入：**
```
2.3,3,5.6,7.6;11,3,8.6,25,1;0.3,9,5.3,66,7.8;1,3,2,7,5;340,670,80.6;<=,<=,<=
```

**输出：**
```
false 458
```

## 解题思路

对输入的一组线性规划问题的求解

###核心知识点

* 从标准输入中读取一行输入，作为线性规划问题的定义；
* 将输入按分号分隔，分别获取不等式约束、不等式目标值、不等式变量以及不等式系数：
* 对于每一个不等式约束，将系数与变量相乘并求和，得到不等式左侧的值，再将其与目标值做差取绝对值，得到不等式的误差；
* 根据不等式约束的类型（大于、小于、大于等于、小于等于），判断该不等式是否成立，同时将误差添加到误差列表中；
* 输出是否满足所有不等式以及误差列表中最大的误差。

## 解题代码

```python
# coding:utf-8
from typing import List
def solve_method(line:str)->None:
    # 接受字符串以 “：”分割
    split1 = line.split(";")
    right = True
    error_list:List[int] = []
    # 倒数第一的限制条件
    limits = split1[-1].split(",")
    # 倒数第二的目标值
    aims = split1[-2].split(",")
    # 倒数第三的变量
    vars_=split1[-3].split(",")
    # 限制条件有几个式子就有几个
    for i in range(len(limits)):
        value =0
        # 将目标值转换为浮点
        aim = float(aims[i])
        #系数
        split_=split1[i].split(",")
        for j in range(len(split_)):
            # 系数乘变量
            value += float(split_[j]) * int(vars_[j])
        limit = limits[i]
        # 取绝对差值
        e = int(abs(value - aim))
        # 匹配限制条件
        if limit ==">":
            right = (value > aim) and right
            error_list.append(e)
        elif limit == "<":
            right = (value < aim) and right
            error_list.append(e)
        elif limit ==">=":
            right = (value >= aim)and right
            error_list.append(e)
        elif limit =="<=":
            right = (value <= aim)and right
            error_list.append(e)
        else:
            right = False
    print(right,max(error_list))

line = input()
solve_method(line)
```

