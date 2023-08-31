# 036 猜字谜

## 题目描述

小王设计了一个简单的猜字谜游戏，游戏的谜面是一个错误的单词，比如`nesw`，玩家需要猜出谜底库中正确的单词。

猜中的要求如下：

对于某个谜面和谜底单词，满足下面任一条件都表示猜中：

- 变换顺序以后是一样的，比如通过变换`w`和`e`的顺序，`nwes`和`news`是可以完全对应的。
- 字母去重以后是一样的，比如`woood`和`wood`是一样的，它们去重后都是`wod`。

请你写一个程序帮忙在谜底库中找到正确的谜底。谜面是多个单词，都需要找到对应的谜底，如果找不到的话，返回`not found`。

## 输入描述

1. 谜面单词列表，以`,`分隔
2. 谜底库单词列表，以`,`分隔
3. 单词的数量N的范围：0 < N < 1000。 
4. 词汇表的数量M的范围： 0 < M < 1000。
5. 单词的长度P的范围：0 < P < 20。 
6. 输入的字符只有小写英文字母，没有其它字符。

## 输出描述

匹配到的正确单词列表，以`,`分隔；如果找不到，返回`not found`。

## 示例描述

### 示例一

**输入：**

```text
conection
connection,today
```

**输出：**
```text
connection
```

### 示例二

**输入：**
```text
bdni,wooood
bind,wrong,wood
```

**输出：**
```text
bind,wood
```


## 解题思路

1. 遍历谜面单词：
    - 将谜面单词转换成小写，然后用`set`去重后排序，记为`str1`。
    - 遍历谜底单词：
        - 将谜底单词转换成小写，然后用`set`去重后排序，记为`str2`。
        - 比较`str1`和`str2`，满足条件，则将谜底单词加入到结果列表中。
    - 如果都没有找到，则本次猜单词的结果为`not found`。
2. 返回结果列表，即为所有对应那个谜面猜测的单词。    

## 解题代码

```python
def solve_method(issues, answers):
    ans = []

    for issue in issues:
        str1 = "".join(sorted(set(issue.lower())))
        find = False

        for answer in answers:
            answer = answer.lower()
            str2 = "".join(sorted(set(answer)))

            if str1 == str2:
                ans.append(answer)
                find = True

        if not find:
            ans.append("not found")

    return ans


if __name__ == '__main__':
    assert solve_method(["conection"], ["connection", "today"]) == ["connection"]
    assert solve_method(["bdni", "wooood"], ["bind", "wrong", "wood"]) == ["bind", "wood"]

```