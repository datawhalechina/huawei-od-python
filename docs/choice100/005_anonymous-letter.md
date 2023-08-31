# 005 匿名信

## 题目描述

电视剧《分界线》里面有一个片段，男主为了向警察透露案件细节，且不暴露自己，于是将报刊上的字剪下来，剪拼成一封匿名信。现在有一名举报人，希望借鉴这种方式，使用英文报刊完成举报操作。但为了增加文章的混淆度，只需满足每个单词中字母数量一致即可，不关注每个字母的顺序。

**解释：** 单词`on`允许通过单词`no`进行替代。

`newspaper`变量表示报纸内容，`anonymousLetter`变量表示匿名信内容，求报纸内容是否可以拼成匿名信。

## 输入描述

- 第一行输入`newspaper`内容，包含`1-N`个字符串，用空格分开。
- 第二行输入`anonymousLetter`内容，包含`1-N`个字符串，用空格分开。
- 注：
    1. `newspaper`和`anonymousLetter`的字符串由小写英文字母组成，且每个字母只能使用一次。
    2. `newspaper`内容中的每个字符串的字母顺序可以任意调整，但必须保证字符串的完整性（每个字符串不能有多余字母）
    3. `1 < N < 100`，`1 <= newspaper.lengh, anonymousLetter.length <= 10^4`

## 输出描述

如果报纸内容可以拼成匿名信，返回`true`，否则返回`false`。

## 示例描述

### 示例一

**输入：**
```text
ab cd
ab
```

**输出：**
```text
true
```

### 示例二

**输入：**
```text
ab ef
aef
```

**输出：**
```text
false
```

### 示例三

**输入：**
```text
ab bcd ef
cbd fe
```

**输出：**
```text
true
```

### 示例四

**输入：**
```text
ab bcd ef
cb fe
```

**输出：**
```text
false
```

## 解题思路

1. 使用`sorted`对报纸和匿名信中的每个单词进行排序。
2. 遍历匿名信中的所有单词，在报纸中寻找单词，如果没有找到，就返回`False`，全部都找到了，最后返回`True`。

## 解题代码

```python
def solve_method(newspaper, anonymousLetter):
    newspaper_list = [sorted(l) for l in newspaper]
    anonymous_letter_list = [sorted(l) for l in anonymousLetter]

    for letter in anonymous_letter_list:
        if letter not in newspaper_list:
            return False

    return True


if __name__ == '__main__':
    newspaper = ["ab", "cd"]
    anonymousLetter = ["ab"]
    assert solve_method(newspaper, anonymousLetter) is True

    newspaper = ["ab", "ef"]
    anonymousLetter = ["aef"]
    assert solve_method(newspaper, anonymousLetter) is False

    newspaper = ["ab", "bcd", "ef"]
    anonymousLetter = ["cbd", "fe"]
    assert solve_method(newspaper, anonymousLetter) is True

    newspaper = ["ab", "bcd", "ef"]
    anonymousLetter = ["cb", "fe"]
    assert solve_method(newspaper, anonymousLetter) is False
```