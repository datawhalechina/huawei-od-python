# 165 相对开音节

## 题目描述

相对开音节构成的结构为:辅音＋元音( `aeiou`) ＋辅音(`r`除外)+`e`。
常见的单词有`bike` 、`cake`等。
给定一个字符串，以空格为分隔符，反转每个单词中的字母，若单词中包含如数字等其他非字母时不进行反转。
反转后计算其中含有相对开音节结构的子串个数(连续的子串中部分字符可以重复)。



## 输入描述

字符串以空格分割的多个单词



`长度<10000`字母只考虑小写



## 输出描述

含有相对开音节结构的子串个数


## 示例描述
### 示例一

**输入：**

```text
ekam a ekac
```

**输出：**

```text
2
```

**说明：**

反转后为`make a cake`其中`make`和`cake`为相对开音节子串

返回`2`



### 示例二

**输入：**

```
!ekam a ekekac
```

**输出：**

```
2
```

**说明：**

反转后为`!ekam a cakeke`

因为 `!ekam`含有非英文字母，所以未反转

其中`cake`和`keke`为相对开音节子串

返回`2`



## 解题思路
**基本思路：**

按照题意进行模拟即可，注意题目的要求，是4个长度的符合要求的字母。

在按照题意翻转完成后，对每个单词进行遍历，遇到e时向前查找三个单词按照题目意思进行判断，不满三个单词直接跳过。



## 解题代码

```python
def solve_method(s):
    # 检查是否合法满足相对元音
    def check(ind, string):
        # 首先长度至少为4
        if ind>=3:
            # ind为e，我们取e前三个字符
            # 首先得是单词字母，其次满足：辅音+元音(aeiou)+辅音(r除外)+e
            substring = string[ind-3:ind]
            # print(substring)
            if substring.isalpha() and substring[0] not in 'aeiou' and substring[1] in 'aeiou' and substring[2] not in 'aeiour':
                return True
        return False
    # 空格切割和反转
    s_list = list(map(lambda x:x[::-1] if x.isalpha() else x, s.split()))
    # print(s_list)
    count = 0
    for string in s_list:
        # 只包含字母
        for ind, char in enumerate(string):
            if char=='e' and check(ind, string):
                count+=1
    return count


if __name__ == '__main__':
    assert solve_method("!ekam a ekekac") == 2
    assert solve_method("ekam a ekac") == 2
    assert solve_method("ekam a ekekac") == 3


```



