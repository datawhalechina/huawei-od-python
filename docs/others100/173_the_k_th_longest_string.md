# 173 第k长子串

## 题目描述

给定一个字符串只包含大写字母，求在包含同一字母的子串中长度第`k`长的子串，相同字母只取最长的子串



## 输入描述

第一行一个子串 `1 < len <= 100`，只包含大写字母

第二行为k的值



## 输出描述

输出连续出现次数第k多的字母的次数

如果子串中只包含同一字母的子串数小于`k`

则输出`-1`



## 示例描述

### 示例一

**输入：**

```text
AABAAA
2
```



**输出：**

```text
1
```

**说明：**

同一字母连续出现最多的`A`:`3`次

第二多也是`A`: `2`次，但A出现连续`3`次，只保留最高的

那么第二多为`B`:`1`次



### 示例二

**输入：**

```text
AAAAHHHBBCDHHHH
3
```



**输出：**

```text
2
```



## 解题思路

**基本思路：**

1. 双指针遍历，将每个字母最长长度存到一个字典里，即{字母: 最长长度}
2. 字典进行从大到小按长度排序
3. 寻找第k长的字母，不存在则返回-1，存在则返回长度

## 解题代码

```python
def solve_method(k, s):
    dic_len = {}
    
    # 双指针，将同一元素最大长度存到dic_len字典中
    left = right = 0
    n = len(s)
    
    count=0
    while right<n:
        if s[left]!=s[right]:
            if s[left] in dic_len:
                dic_len[s[left]] = max(dic_len[s[left]], right-left)
            else:
                dic_len[s[left]] = right-left
            left = right
        right+=1
    if s[left] in dic_len:
        dic_len[s[left]] = max(dic_len[s[left]], right-left)
    else:
        dic_len[s[left]] = right-left

    # 将字典转化成元祖，按照长度从大到小进行排序
    tuple_len = sorted(dic_len.items(), key=lambda x:-x[1])
    # 记录总长度n
    n = len(tuple_len)
    
    # 子串数小于k，找不到返回-1
    if k-1>=n:
        return -1
    else:
        return tuple_len[k-1][1]


if __name__ == '__main__':
    assert solve_method(2, "AABAAA") == 1
    assert solve_method(3, "AAAAHHHBBCDHHHH") == 2
```



