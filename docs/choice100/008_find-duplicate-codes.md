# 008 找出重复代码

## 题目描述

小明负责维护项目下的代码，需要查找出重复代码，用以支撑后续的代码优化，请你帮助小明找出重复的代码。

重复代码查找方法：以字符串形式给出两行代码（字符串长度`1 < length <= 100`，由英文字母、数字和空格组成），找出两行代码中的最长公共子串。

注：如果不存在公共子串，返回空字符串。

## 输入描述

输入的参数`text1`、`text2`分别代表两行代码。

## 输出描述

输出任一最长公共子串。

## 示例描述

### 示例一

**输入：**
```text
hello123world
hello123abc4
```

**输出：**
```text
hello123
```

### 示例二

**输入：**
```text
private_void_method
public_void_method
```

**输出：**
```text
_void_method
```

### 示例三

**输入：**
```text
hiworld
hiweb
```

**输出：**
```text
hiw
```

## 解题思路

1. 本题采用动态规划方法进行解题
2. 确定dp数组以及下标的含义：
   dp[i][j]：⻓度为[0, i - 1]的字符串text1与⻓度为[0, j - 1]的字符串text2的最⻓公共⼦序列为dp[i][j]
3. 确定递推公式：
   - 如果text1[i - 1] 与 text2[j - 1]相同，那么找到了⼀个公共元素，所以dp[i][j] = dp[i - 1][j - 1] + 1;
   - 如果text1[i - 1] 与 text2[j - 1]不相同，那就看看text1[0, i - 2]与text2[0, j - 1]的最⻓公共⼦序列和text1[0, i - 1]与text2[0, j - 2]的最⻓公共⼦序列，取最⼤的。
4. dp数组初始化：dp[i][0] = 0，dp[0][j] = 0;
5. 确定遍历顺序：从前向后，从上到下遍历矩阵
6. 获取最大长度`max_length`，并保存字符串的尾指针`end`
7. 根据尾指针`end`和最大长度`max_length`，返回最长公共子串。
     
## 解题代码

```python
def solve_method(text1, text2):
    dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
    end = 0
    max_length = 0
    for i in range(1, len(text1) + 1):
        for j in range(1, len(text2) + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                # 获取最大长度
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end = i - 1
    # 返回最长公共子串                
    return text1[end - max_length + 1: end + 1]


if __name__ == '__main__':
    assert solve_method("hello123world", "hello123abc4") == "hello123"
    assert solve_method("private_void_method", "public_void_method") == "_void_method"
    assert solve_method("hiworld", "hiweb") == "hiw"
```