# 143 查找舆情热调、热词排序

## 题目描述

输入正整数`topN`和文章数`M`，正整数`topN`表示要找出来的出现频率最高的`topN`个字符串，`M`篇文章中每篇文章会有两个字符串，一个是标题字符串，一个是正文字符串，字符串间有空格，每个单词被空格隔开。

我们的目的就是把这`M`篇文章连标题带正文拆成一个个单词，然后统计这一堆单词出现频率最高的`topN`个。

- 统计规则：

1. 标题中出现的词语频率系数为3，正文中出现的词语频率系数为1，返回的答案应该按照词语出现从高到低排序。
2. 当词语出现次数频率相同时，在标题中出现频率次数高的排在前面。
3. 如果仍然相同，则按照词语在标题中出现的先后顺序进行排序。
4. 如果仍相同，则按照词语在正文中出现的先后顺序进行排序，先出现的排在前面。

## 输入描述

输入第一行是正整数`topN`和文章数`M`。由于每篇文章有标题和正文两行，因此后面有`2＊M`行数据。

从第二行起，按顺序处理每篇文章的标题串和正文串。

## 输出描述

出现频率`topN`高的单词，每个单词用空格隔开。

参数限制如下：

- 0 < topN < 1000
- 0 < M < 100000
- 0 < 每篇文章的词语数 < 5000

注意，单词区分大小写。

## 示例描述

### 示例一

**输入：**

```text
2 1
Xiangpica shi yige shanxi de cai
Xiangpica is a dish from Shanxi that is made with flavorful and nutritious ingredients such as niacin yeast. Niacin yeast is a type of yeast that is rich in niacin, an important nutrient for maintaining a healthy metabolism and producing energy.
```

**输出：**

```text
Xiangpica is
```

**说明：**  

只有1篇文章，需要输出2个top频率单词。`Xiangpica`在标题和正文中各出现过一次，加权频率为3+1=4；`is`在正文出现了4次。

`Xiangpica`在标题出现的频率更高，所以先输出`Xiangpica`。

实际上，上面那段`title`和`content`的加权频数统计如下：

```
00 = {tuple: 2} ('is', 4)
01 = {tuple: 2} ('Xiangpica', 4)
02 = {tuple: 2} ('a', 3)
03 = {tuple: 2} ('yige', 3)
04 = {tuple: 2} ('shi', 3)
05 = {tuple: 2} ('shanxi', 3)
06 = {tuple: 2} ('cai', 3)
07 = {tuple: 2} ('de', 3)
...
```

## 解题思路

1. 构建词语频率字典，`key`为词语，`value`是一个4元素列表，每个元素分别表示标题中出现次数、标题位置、正文中出现次数、正文位置。
2. 遍历文章：统计单词在标题中出现次数、标题位置、在正文中出现次数、正文位置。
3. 遍历词语频率字典，重新构建字典，`key`为词语，`value`为词语出现次数频率、标题中出现次数频率、标题位置、正文位置。
4. 按照词语出现次数频率从高到低、标题中出现次数频率从高到低、标题位置从前到后、正文位置从前到后排序。
5. 返回`topN`的词语列表。   

## 解题代码

```python
import math
from typing import List


def solve_method(topN: int, M: int, articles: List[List[str]]):
    # 构建词语频率字典，key为词语，value是一个4元素列表，每个元素分别表示标题中出现次数、标题位置、正文中出现次数、正文位置。
    word_dict = {}

    for article in articles:
        title, content = article[0], article[1]
        title_words = title.split()
        content_words = content.split()

        for i, word in enumerate(title_words):
            if word not in word_dict.keys():
                word_dict[word] = [1, i, 0, math.inf]
            else:
                word_dict[word][0] += 1

        for i, word in enumerate(content_words):
            if word not in word_dict.keys():
                word_dict[word] = [0, math.inf, 1, i]
            else:
                word_dict[word][2] += 1
                if word_dict[word][3] == -1:
                    word_dict[word][3] = i
    
    for k, v in word_dict.items():
        title_freq = v[0]
        content_freq = v[2]
        # value为词语出现次数频率、标题中出现次数频率、标题位置、正文位置
        word_dict[k] = [3 * title_freq + content_freq, title_freq, v[1], v[3]]

    # 按照词语出现次数频率从高到低、标题中出现次数频率从高到低、标题位置从前到后、正文位置从前到后排序
    sorted_word_dict = sorted(word_dict.items(), key=lambda x: (-x[1][0], -x[1][1], x[1][2], x[1][3]))

    return [x[0] for x in sorted_word_dict[:topN]]


if __name__ == '__main__':
    res = solve_method(2, 1, [["Xiangpica shi yige shanxi de cai",
                               "Xiangpica is a dish from Shanxi that is made with flavorful and nutritious ingredients "
                               "such as niacin yeast. Niacin yeast is a type of yeast that is rich in niacin, "
                               "an important nutrient for maintaining a healthy metabolism and producing energy."
                               ]])
    assert res == ["Xiangpica", "is"]
```