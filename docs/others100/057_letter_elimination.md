# 57 字母消消乐

## 题目描述

游戏规则:
输入一个只包含英文字母的字符串，字符串中的两个字母如果相邻且相同,就可以消除。在字符串上反复执行消除的动作，直到无法继续消除为止,此时游戏结束。输出最终得到的字符串长度。



## 输入描述

输入原始字符串`str`

只能包含大小写英文字母，字母的大小写敏感，`str`长度不超过100

## 输出描述

输出游戏结束后,最终得到的字符串长度



## 示例描述

### 示例一

**输入：**

```text
gg
```



**输出：**

```text
0
```

说明：
`gg` 可以直接消除，得到空串，长度为`0`

### 示例二

**输入：**

```text
mMbccbc
```



**输出：**

```text
3
```

说明：

`mMbccbc`中，可以先消除`cc`此时变为`mMbbc`，再消除，`bb`，此时变成`mMc`
此时没有相同且相邻的字符无法继续消除，最终得到字符串`mMc`，长度为`3`

## 备注
输入中包含非大小写英文字母时，均为异常输入，直接返回0



## 解题思路

**基本思路：**

1. 在一个while死循环中，先记录当前s的长度
2. 遍历s遇到相邻就删除，记录删除后的s的长度
3. 如果s当前长度和之前的长度相同，则退出while循环
4. 否则继续while循环而继续删除下一个相邻字母

## 解题代码

```python
def solve_method(m_str):
    # 使用列表推导式仅保留字母字符
    linked_list = [c for c in m_str if c.isalpha()]

    i = 0
    # 通过比较相邻字符并删除重复项来迭代列表
    while linked_list < len(linked_list):
        if linked_list[i] == linked_list[i + 1]:
            del linked_list[i:i + 2]
            i = max(0, i - 1)
        else:
            i += 1
    return len(linked_list)


if __name__ == '__main__':
    # 去掉首尾空字符串并且输入
    m_str = input().strip()
    print(solve_method(m_str))
```



