# 301 AI处理器组合

## 题目描述
小华负责公司知识图谱产品，现在要通过新词挖掘完善知识图谱。 \
新词挖掘：给出一个待挖掘文本内容字符串content和一个词的字符串word，找到content中所有word的新词。 \
新词：使用词word的字符排列形成的字符串。 \
请帮小华实现新词挖掘，返回发现的新词的数量。

## 输入描述
第一行输入为待挖掘的文本内容content； \
第二行输入为词word； \
$0≤content.length≤10000000$；\
$1≤word.length≤2000$

## 输出描述
在中找到的所有word的新词的数量。

### 示例一
**输入：**
```shell
qweebaewqd
qwe
```

**输出：**
```shell
2
```

**说明：**  
起始索引等于 0 的子串是 qwe, 它是 word的新词。 \
起始索引等于 6 的子串是 ewq, 它是 word的新词。



### 示例二
**输入：**
```shell
abab
ab
```

**输出：**
```shell
3
```

**说明：**  
起始索引等于 0 的子串是 ab, 它是 word 的新词。 \
起始索引等于 1 的子串是 ba, 它是 word 的新词。 \
起始索引等于 2 的子串是 ab, 它是 word 的新词。
## 解题思路
1. 首先，我们需要计算目标词的每个字符的频率。为此，我们可以遍历目标词的每个字符，然后在一个长度为26的数组中记录每个字符的出现次数。这样，我们可以根据字母的ASCII码计算出该字母在数组中的索引。
2. 然后，我们需要遍历文本内容中的所有长度与目标词长度相同的子串。为了实现这一点，我们可以使用一个简单的for循环，从0开始，直到文本内容的长度减去目标词的长度。
3. 对于每个子串，我们需要判断它是否是目标词的新词。为此，我们可以计算子串中每个字符的频率，然后将其与目标词的字符频率进行比较。如果两者相同，则子串是目标词的新词。
4. 如果子串是目标词的新词，我们可以将新词的数量加1。
5. 最后，返回新词的总数。

## 解题代码

```python
def is_new_word(word, char_count):
    temp_char_count = [0] * 26
    for ch in word:
        temp_char_count[ord(ch) - ord('a')] += 1

    for i in range(26):
        if char_count[i] != temp_char_count[i]:
            return False
    return True

def new_word_discovery(content, word):
    word_length = len(word)
    content_length = len(content)
    char_count = [0] * 26
    new_word_count = 0

    for ch in word:
        char_count[ord(ch) - ord('a')] += 1

    for i in range(content_length - word_length + 1):
        if is_new_word(content[i:i + word_length], char_count):
            new_word_count += 1
    return new_word_count

content = input().strip()
word = input().strip()

result = new_word_discovery(content, word)
print(result)
```