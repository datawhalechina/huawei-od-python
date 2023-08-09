# 171 符合条件的子串长度

## 题目描述

给定字符串`A`、`B`和正整数`V`，字符串`A`和`B`的长度相等，计算`A`中满足如下条件的最大连续子串的长度:

1. 该连续子串在`A`和`B`中的位置和长度相同。
2. 该连续子串`|A[i]- B[i]|`(两个字母ASCII码之差的绝对值)之和小于等于`V`



## 输入描述

第一行输入字符串`A`，仅包含小写字母，`1 <= A.length <= 1000`

第二行输入字符串`B`，仅包含小写字母，`1 <= B.length <= 1000`

第三行输入正整数`V`，`0 <= V <= 10000`



## 输出描述

字符串最大连续子串的长度，要求该子串`|A[i]- B[i]|`之和小于等于v



## 示例描述

### 示例一

**输入：**

```text
xxcdefg
cdefghi
5
```



**输出：**

```text
2
```



## 解题思路

**基本思路：**

1. 先根据ASCII码值，使用ord函数求出一个差值list

2. 再根据差值list用双指针求最大长度

## 解题代码

```python
def solve_method(s1, s2, v):
    res = []
    n = len(s1)
    for i in range(n):
        res.append(abs(ord(s1[i])-ord(s2[i])))
    # 两个指针
    left =right= 0
    # 记录累加和
    accu = 0
    # 记录最大长度
    max_len = 0
    while right<n:
        accu+=res[right]
        # 累加和accu超过了v，左端点右移，accu减去相应的值
        while accu>v:
            accu-=res[left]
            left+=1
        max_len=max(max_len, right-left+1)
        right+=1
    return max_len


if __name__ == '__main__':
    assert solve_method("xxcdefgx", "cdefghic",5) == 2
```



