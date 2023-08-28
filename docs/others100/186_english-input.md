# 186 英文输入法

## 题目描述

主管期望你来实现英文输入法单词联想功能，需求如下：

1. 依据用户输入的单词前缀，从已输入的英文语句中联想出用户想输入的单词。
2. 按字典序输出联想到的单词序列，如果联想不到，请输出用户输入的单词前缀。

**注意：**

1. 英文单词联想时区分大小写。
2. 缩略形式如`don't`判定为两个单词`don`和`t`。
3. 输出的单词序列不能有重复单词，且只能是英文单词，不能有标点符号。

## 输入描述

第一行输入一段由英文单词`word`和标点构成的语句`str`。取值范围是0 < word.length() <= 20、0 < str.length() <= 10000。

接下来一行是一个英文单词前缀`pre`。前缀长度的取值范围是0 < pre.length() <= 20

## 输出描述

输出符合要求的单词序列或单词前缀存在多个时，单词之间以单个空格分隔。 

## 示例描述

### 示例一

**输入：**

```text
I love you
He
```

**输出：**

```text
He
```

**说明：**

用户已输入单词语句`I love you`，从中提炼出`I`、`love`、`you`三个单词。

接下来，用户输入`He`，从已经输入信息中，无法联想到符合要求的单词，所以输出用户输入的单词前缀。

### 示例二

**输入：**

```text
The furthest distance in the world,Is not between life and death,But when I stand in front or you,Yet you don't know that I love you.
f
```

**输出：**

```text
front furthest
```

## 解题思路

1. 使用正则表达式，获取所有的单词（如果遇到缩略形式，判定为两个单词），存入列表`words`。
2. 对`words`使用`set`进行去重。
3. 遍历列表：当单词满足前缀，则加入结果列表中。
4. 对结果列表进行字典序排序。
5. 返回结果列表拼接成的字符串。

## 解题代码

```python
import re


def solve_method(line, pre):
    words = re.findall(r'\w+', line)
    word_set = set(words)

    result = []

    for word in word_set:
        if word.startswith(pre):
            result.append(word)
    if not result:
        result.append(pre)

    result.sort()
    return " ".join(result)


if __name__ == '__main__':
    assert solve_method("I love you", "He") == "He"

    line = """The furthest distance in the world,
              Is not between life and death,
              But when I stand in front or you,
              Yet you don't know that I love you. """
    assert solve_method(line, "f") == "front furthest"
```

