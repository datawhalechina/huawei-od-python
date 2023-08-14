# 175 简易压缩算法

## 题目描述

有一种简易压缩算法:针对全部为小写英文字母组成的字符串，将其中连续超过两个相同字母的部分压缩为连续个数加该字母，其他部分保持原样不变，例如字符串`aaabbccccd`经过压缩变成字符串`3abb4cd`。请您编写解压函数,根据输入的字符串：

- 判断其是否为合法压缩过的字符串。
- 若输入合法则输出解压缩后的字符串。
- 否则输出字符串`!error`来报告错误



## 输入描述

输入一行，为一个ASCIl字符串

长度不超过`100`字符

用例保证输出的字符串长度也不会超过`100`字符串



## 输出描述

若判断输入为合法的经过压缩后的字符串

则输出压缩前的字符串

若输入不合法则输出字符串`!error`



## 示例描述

### 示例一

**输入：**

```text
4dff
```



**输出：**

```text
ddddff
```

**说明：**

4d扩展为4个d，故解压后的字符串为ddddff



### 示例二

**输入：**

```text
2dff
```



**输出：**

```text
!error
```

**说明：**

2个d不需要压缩故输入不合法



### 示例三

**输入：**

```text
4d@A
```



**输出：**

```text
!error
```

**说明：**

全部由小写英文字母做成的字符串，压缩后不会出现特殊字符@和大写字母A故输入不合法





## 解题思路

**基本思路：**

1. 先对输入进行一遍过滤，判断是否只由数字和小写字母组成
2. 将配对的数字和字母组合或者多个相同的字母组合，存在stack中
3. 遍历stack，对每个组合进行校验，正确则按照数字倍数增长或者纯字母拼到结果中，否则校验失败则直接返回'!error'

## 解题代码

```python
def solve_method(s):
    stack = []

    # 1.初筛
    # 先判断是否是数字和小写字母
    for i in s:
        if i.isdigit() or (i.isalpha() and i.islower()):
            continue
        else:
            return '!error'
    
    # 2.将数字和字母配对在一起
    stack = []
    for i in s:
        if stack:
            # 数字相邻则相连
            if i.isdigit():
                if stack[-1].isdigit():
                    stack[-1]+=i
                    continue
            # 字母前是数字则相连，字母前是相同的字母则相连
            else:
                if stack[-1].isdigit() or stack[-1][-1]==i:
                    stack[-1]+=i
                    continue
        # 其余情况直接append
        stack.append(i)
        
    # 将配对的数字和字母组合到一起，存在stack中
    # print(stack)

    # 3.遍历整个stack内的元素，同时判断元素是否合法
    res = ''
    for string in stack:
        num = ''
        alpha = ''
        for char in string:
            if char.isdigit():
                num+=char
            else:
                alpha+=char
        # 不合法的规则：既有数字，还有两个字母；或者字母数量大于2
        if (num and len(alpha)==2) or (len(alpha)>2):
            return '!error'
        else:
            if num:
                res+=alpha*int(num)
            else:
                res+=alpha
    return res

if __name__ == '__main__':
    assert solve_method("4dff2d") == 'ddddffdd'
    assert solve_method("24d2ff2d") == '!error'
    assert solve_method("24dfff2d") == '!error'
    assert solve_method("4#dff2dabcd") == '!error'
```



