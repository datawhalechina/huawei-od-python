# 078 找出同班小朋友

## 题目描述
幼儿园两个班的小朋友排队时混在了一起，
每个小朋友都知道自己跟前面一个小朋友是不是同班，请你帮忙把同班的小朋友找出来。
小朋友的编号为整数，
与前面一个小朋友同班用Y表示不同班用N表示。


## 输入描述
输入为空格分开的小朋友编号和是否同班标志比如6/N 2/Y 3/N 4/Y，
表示一共有4位小朋友，
2和6是同班，3和2不同班，4和3同班。小朋友总数不超过999，
0 < 每个小朋友编号 < 999，
不考虑输入格式错误

## 输出描述
每一行记录一班小朋友的编号，编号用空格分开并且：
1. 编号需要按照大小升序排列，分班记录中第一个编号小的排在第一行
2. 如果只有一个班的小朋友第二行为空
3. 如果输入不符合要求输出字符串ERROR

## 示例描述

### 示例一

**输入：**
```text
1/N 2/Y 3/N 4/Y
```

**输出：**
```text
1 2
3 4
```
**说明**
2的同班标记为Y因此和1同班，
3的同班标记位N因此和1,2不同班，4的同班标记位Y因此和3同班。

## 解题代码

```python
#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 078_find-same-class-children
@time:  23/8/2023 下午 11:57
@project:  huawei-od-python 
"""


def solve_method(s):
    try:
        queue = s.split(' ')
        class1, class2 = [int(queue.pop(0).split('/')[0])], []
        prev = 1
        while queue:
            id_, flag = queue.pop(0).split('/')
            if (flag == 'Y' and prev == 1) or (flag == 'N' and prev == 2):
                class1.append(int(id_))
                prev = 1
            else:
                class2.append(int(id_))
                prev = 2
        class1 = sorted(class1)
        class2 = sorted(class2)
        if class1[0] < class2[0]:
            return '\n'.join([' '.join(map(str, class1)), ' '.join(map(str, class2))])
        else:
            return '\n'.join([' '.join(map(str, class2)), ' '.join(map(str, class1))])
    except:
        return 'ERROR'


if __name__ == '__main__':
    s = input().strip()
    res = solve_method(s)
    print(res)
```

