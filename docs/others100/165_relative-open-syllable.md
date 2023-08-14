# 165 相对开音节

## 题目描述

相对开音节构成的结构为：辅音+元音(`aeiou`)+辅音(`r`除外)+`e`。常见的单词有`bike`、`cake`等。

给定一个字符串，以空格为分隔符，反转每个单词中的字母，若单词中包含如数字等其他非字母时不进行反转。反转后，计算其中含有相对开音节结构的子串个数（连续的子串中部分字符可以重复）。

## 输入描述

字符串以空格分隔的多个单词，其中字符串长度小于10000，字母只考虑小写。

## 输出描述

含有相对开音节结构的子串个数。

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

反转后为`make a cake`，其中`make`和`cake`为相对开音节子串，返回2。

### 示例二

**输入：**

```text
!ekam a ekekac
```

**输出：**

```text
2
```

**说明：**

反转后为`!ekam a cakeke`，因为 `!ekam`含有非英文字母，所以未反转。其中`cake`和`keke`为相对开音节子串，返回2。

## 解题思路

1. 对字符串进行空格分隔和反转。
2. 针对相对开音节的规则，使用正则表达式`[^aeiou][aeiou][^aeiour]e`。
3. 遍历所有单词：
    - 判断是否全部为字母。
    - 根据正则表达式，判断是否满足条件。
    - 如果都成立，计数器累计加1。
4. 返回计数器的结果值。    

## 解题代码

```python
import re


def solve_method(line):
    # 空格分隔和反转
    s_list = list(map(lambda x: x[::-1] if x.isalpha() else x, line.split()))
    count = 0
    p = re.compile(r"[^aeiou][aeiou][^aeiour]e")
    for string in s_list:
        # 必须全部是字母，才符合要求
        if len(string) >= 4 and all([True if ch.isalpha() else False for ch in string]):
            for i in range(len(string) - 3):
                # 使用正则表达式判断是否满足条件
                result = p.search(string[i:i + 4])
                if result:
                    count += 1

    return count


if __name__ == '__main__':
    assert solve_method("ekam a ekac") == 2
    assert solve_method("!ekam a ekekac") == 2
```



