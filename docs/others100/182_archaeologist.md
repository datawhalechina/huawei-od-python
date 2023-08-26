# 182 考古学家

## 题目描述

有一个考古学家发现一个石碑，但是很可惜发现时其已经断成多段，原地发现`N`个断口整齐的石碑碎片，为了破解石碑内容，考古学家希望有程序能帮忙计算复原后的石碑文字组合数，你能帮忙吗？

## 输入描述

第一行输入`N`，`N`表示石碑碎片的个数。

第二行依次输入石碑碎片上的文字内容`S`，共有`N`组。

## 输出描述

输出石碑文字的组合（按照升序排列一），行尾无多余空格。

## 示例描述

### 示例一

**输入：**
```text
3
a b c
```

**输出：**
```text
abc
acb
bac
bca
cab
cba
```

### 示例二

**输入：**
```text
3
a b a
```

**输出：**
```text
aab
aba
baa
```

### 示例三

**输入：**
```text
3
a b ab
```

**输出：**
```text
aabb
abab
abba
baab
baba
```

## 解题思路

对字符串segment进行分割，得到一个字符串列表segments ;
使用itertools , permutations函数计算字符串列表segments的全排列，并将结果存储在_permutation_list 中;。将permutation_list中的所有元素组合成一个字符串，并去重，得到新的字符串列表;

## 解题代码

```python
import itertools
def solve_method(n,segment):
    segement = segment.split(" ")
    #使用itertools.permutations函数对segement列表进行排列组合，返回一个包含所有可能排列的列表permutation_list
    permutation_list = list(itertools.permutations(segement))
    #通过列表推导式和set函数，将permutation_list中的元组转换为字符串，并去除重复的元素。
    permutation_list = list(set(["".join(i) for i in permutation_list]))
    permutation_list.sort()
    for item in permutation_list:
        print(item)

def main():
    n=int(input().strip())
    segment = input().strip()
    solve_method(n,segment)

if __name__ == '__main__':
    main()
        
    
```

