# 026 关联字串

## 题目描述

给定两个字符串 `str1`和 `str2`
如果字符串 `str1` 中的字符，经过排列组合后的字符串中
只要有一个是 `str2` 的子串
则认为 `str1` 是 `str2` 的关联子串
若不是关联子串则返回 -1
预制条件:
1.输入的字符串只包含小写字母
2.两个字符串的长度范围 `1 ~ 100000`
3.若 `str2` 中有多个 `str1` 的组合子串，请返回第一个子串的起始位置
备注: 输入字符串只包含小写，长度 `1~100000`

## 输入描述

输入两个字符串，分别为题目中描述的 `str1`和 `str2`

## 输出描述

如果 `str1` 是 `str2` 的关联子串，则返回子串在 `str2` 中的起始位置
如果不是则返回 `-1`
若 `str2` 中有多个 `str1` 的组合子串,请返回最小的起始位置

## 示例描述

### 示例一

**输入：**

```Plain Text
abc efghicabiii
```

**输出：**

```Plain Text
5
```

**说明：**
`str2` 包含 `str1` 的一种排列组合( `cab` )
其在 `str2` 的起始位置为 `5`(从 开始计数)

### 示例二

**输入：**

```Plain Text
abc  efghicaibii
```

**输出：**

```Plain Text
-1
```

**说明：
`'**abc'`字符串中三个字母的各种组合`(abc'，acb'，bac’，bca'，cab ，cba')`，`str2`中均不包含因此返回`-1`

## 解题思路

**基本思路：** 

1. 根据字符串`str1`的长度对字符串`str2[i:i+length]`的字符进行读取，存于`temp`中

2. 然后逐个读取`str1[j]`的字符，判断是否与`temp`的元素一样，
如果是清空temp返回结果
如果不是则继续执行程序

3. 如果遍历完不存在则返回-1

## 解题代码

```Python
def solve(str1, str2):
    length = len(str1)
    temp = []
    for i in range(len(str2) - length + 1):
        temp = list(str2[i:i+length])
        j = 0
        while j < length:
            if str1[j] in temp:
                temp.remove(str1[j])
            j += 1
        if temp == []:
            return i
    return -1

if __name__ == '__main__':
    str1 = input()
    str2 = input()
    result = solve(str1, str2)
    print(result) 
```

