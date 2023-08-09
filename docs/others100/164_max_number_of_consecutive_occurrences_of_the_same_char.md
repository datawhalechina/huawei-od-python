# 164 相同字符连续出现的最大次数

## 题目描述

输入—串字符串
字符串长度不超过`180`
查找字符串中相同字符连续出现的最大次数



## 输入描述

输入只有一行，包含一个长度不超过100的字符串


## 输出描述

输出只有一行，输出相同字符串连续出现的最大次数


## 示例描述
### 示例一

**输入：**

```text
hello
```

**输出：**

```text
2
```



### 示例二

**输入：**

```text
word
```

**输出：**

```text
1
```

### 示例三

**输入：**

```text
aaabbc
```

**输出：**

```text
3
```



## 解题思路
**基本思路：**

思路很清晰，双指针从左向右遍历，统计每个相同子串的长度并更新最大长度



## 解题代码

```python
def solve_method(s):
    # 双指针
    left = right = 0
    # 求最大值则初始化一个负无穷，当然也可以为0
    max_v = -float('inf')

    # 双指针模板
    count = 0
    while right<len(s):
        # 遇到相同字符指针右移，次数+1
        if s[left]==s[right]:
            count+=1
            right+=1
        # 遇到不相同字符，统计left字符的count
        # 更新最大值，随后left移到新字符上，count归零
        else:
            max_v = max(max_v, right-left)
            left=right
            count=0
    # 循环外结尾的字符还要更新一次，因为退出时没有进入while内的更新部分
    max_v = max(max_v, right-left)
    return max_v


if __name__ == '__main__':
    assert solve_method("aaabbc") == 3
    assert solve_method("aaabbccccc") == 5
    assert solve_method("aaabbcccccbbbbbbaaaaa") == 6
```



