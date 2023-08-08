# 143 查找舆情热调、热词排序

## 题目描述

输入正整数topN和文章数M，正整数topN表示要找出来的出现频率最高的topN个字符串，M篇文章中每篇文章会有两个字符串，一个是标题字符串，一个是正文字符串，字符串间有空格，每个单词被空格隔开。

我们的目的就是把这M篇文章连标题带正文拆成一个个单词，然后统计这一堆单词出现频率最高的topN个。



- 统计规则：

1. 标题中出现的词语频率系数为3，正文中出现的词语频率系数为1，返回的答案应该按照词语出现从高到低排序。（逆序）

2. 当词语出现次数频率相同时，在标题中出现频率次数高的排在前面；（逆序）
3. 如果仍然相同，则按照词语在标题中出现的先后顺序进行排序；（每个单词记录最小、最先出现的值）
4. 如果仍相同，则按照词语在正文中出现的先后顺序进行排序，先出现的排在前面。（每个单词记录最小、最先出现的值）



## 输入描述

第一行输入为正整数topN和文章数M。

由于每篇文章有标题和正文两行，因此后面有2＊M行数据。

从第二行起，按顺序处理每篇文章的标题串和正文串。



## 输出描述

出现频率topN高的单词，每个单词用空格**' '**隔开。

参数限制如下：

- 0 < topN < 1000

- 0 < M < 100000

- 0＜每篇文章的词语数＜5000

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

只有1篇文章，需要输出2个top频率单词。

Xiangpica在标题和正文中各出现过一次，加权频率为3+1=4；

is 在正文出现了4次。

Xiangpica在标题出现的频率更高，所以先输出Xiangpica。

实际上，上面那段title和content的加权频数统计如下：

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

**基本思路：** 

- 可以使用Python的collections库中的Counter类来统计单词出现的频率；使用哈希表（Python的字典数据结构）记录关键数据。
- 我们分别统计单词在标题里、在正文里出现的次数、在标题中出现的先后顺序、在正文中出现的先后顺序，然后按照题目要求，将单词按多键值排序后，输出排在最前的N个单词即可。
- 多键值排序可以借用sorted函数和自定义比较函数
  - `    sorted_words = sorted(freq.keys(), key=cmp_to_key(compare_function))`
- 在调用字典的get()方法时，注意提供默认值。

## 解题代码

```python
from functools import cmp_to_key
from typing import List
from collections import Counter


def solve_method(topN: int, M: int, data: List[str]) -> str:
    # 单词的加权频数
    freq = {}

    # 单词的标题频数
    word_freq_title = {}

    # 单词在标题中的先后顺序（每个单词记录最小）
    word_appear_title_no = {}

    # 单词在正文中的先后顺序（每个单词记录最小）
    word_appear_content_no = {}

    for i in range(M):
        title, content = data[i * 2].split(), data[i * 2 + 1].split()
        words = set(title).union(content)
        title_counter = Counter(title)
        content_counter = Counter(content)

        for word in words:
            # 统计规则1，计算加权总频数，标题加权系数为3，正文系数为1
            freq[word] = freq.get(word, 0) + title_counter.get(word, 0) * 3
            freq[word] = freq.get(word, 0) + content_counter.get(word, 0)

            # 统计规则2：更新单词的标题频数
            word_freq_title[word] = word_freq_title.get(word, 0) + title_counter.get(word, 0)

            # 统计规则3：单词在标题中的先后顺序（每个单词记录最小
            first_appear_in_title = -1 if word not in title else title.index(word)
            if first_appear_in_title != -1:
                word_appear_title_no[word] = min(first_appear_in_title, word_appear_title_no.get(word, 9999))

            # 统计规则4：单词在正文中的先后顺序（每个单词记录最小
            first_appear_in_content = -1 if word not in content else content.index(word)
            if first_appear_in_content != -1:
                word_appear_content_no[word] = min(first_appear_in_content, word_appear_content_no.get(word, 9999))

    # 定义一个比较函数，用于自定义单词顺序
    def compare_function(word1, word2):
        if word1== word2:
            return 0

        # 规则1: 标题中出现的词语频率系数为3，正文中出现的词语频率系数为1，返回的答案应该按加权频数逆序排列
        condition1 = freq.get(word1) - freq.get(word2)
        if condition1 != 0:
            return -1 * condition1

        # 规则2：当词语出现次数频率相同时，在标题中出现频率次数高的排在前面；（逆序）
        condition2 = word_freq_title.get(word1) - word_freq_title.get(word2)
        if condition2 != 0:
            return -1 * condition2

        # 规则3：如果仍然相同，则按照词语在标题中出现的先后顺序进行排序；（顺序）
        condition3 = word_appear_title_no.get(word1, 9999) - word_appear_title_no.get(word2, 9999)
        if condition3 != 0:
            return condition3

        # 规则4：如果仍相同，则按照词语在正文中出现的先后顺序进行排序，先出现的排在前面。
        condition4 = word_appear_content_no.get(word1, 9999) - word_appear_content_no.get(word2, 9999)
        if condition4 != 0:
            return condition4

    # 使用比较函数
    sorted_words = sorted(freq.keys(), key=cmp_to_key(compare_function))

    result = ' '.join([sorted_words[i] for i in range(topN)])
    return result
```