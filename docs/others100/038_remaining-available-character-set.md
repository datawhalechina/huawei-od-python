# 038 剩余可用字符集

## 题目描述

给定两个字符集合，一个是全量字符集，一个是已占用字符集，已占用字符集中的字符不能再使用，要求输出剩余可用字符集。

## 输入描述

1. 输入一个字符串，一定包含`@`，`@`前为全量字符集，`@` 后的为已占用字符集。
2. 已占用字符集中的字符，一定是全量字符集中的字符，字符集中的字符跟字符之间使用`,`分隔。
3. 每个字符都表示为字符+数字的形式，用`:`分隔，比如`a:1`表示1个`a`字符。
4. 字符只考虑英文字母，区分大小写，数字只考虑正整型，不超过100。
5. 如果一个字符都没被占用，`@`标识仍存在，例如`a:3,b:5,c:2@`

## 输出描述

输出可用字符集，不同的输出字符集之间用回车换行。

注意： 输出的字符顺序要跟输入的一致，不能输出`b:3,a:2,c:2`，如果某个字符已全部占用，则不需要再输出。

## 示例描述

### 示例一

**输入：**
 
```text
a:3,b:5,c:2@a:1,b:2
```

**输出：**

```text
a:2,b:3,c:2
```

**说明：**

全量字符集为3个`a`、5个`b`、2个`c`，已占用字符集为1个`a`、2个`b`。

由于已占用字符不能再使用，所以剩余可用字符为2个`a`、3个`b`、2个`c`。

因此输出`a:2,b:3,c:2`。

## 解题思路

基本思路：

1. 将输入字符串按照`@`进行分隔，并将结果分别赋值给全量字符集`totals`和已占用`useds`。
2. 分别遍历`total`和`used`，对每对键值进行拆分，并将每对第二个元素转为整数类型，存于`total_map`和`used_map`。
3. 遍历`used_map`中的字符，并与`total_map`中的字符进行计算，求出剩余量：
    - 如果剩余量是正数，则更新
    - 如果剩余量小于等于0，则删除该字符
4. 返回结果。

## 解题代码

```Python
def solve_method(line):
    total, used = line.split("@")

    def to_counter(chars):
        chars = chars.split(",")
        chars_map = {}
        for char in chars:
            char = char.split(":")
            chars_map[char[0]] = int(char[1])
        return chars_map

    total_map = to_counter(total)
    if used:
        used_map = to_counter(used)
        for k in used_map.keys():
            diff = total_map[k] - used_map[k]
            if diff > 0:
                total_map[k] = diff
            else:
                total_map.pop(k)

    return ",".join([k + ":" + str(v) for k, v in total_map.items()])


if __name__ == '__main__':
    assert solve_method("a:3,b:5,c:2@a:1,b:2") == "a:2,b:3,c:2"
    assert solve_method("a:3,b:5,c:2@") == "a:3,b:5,c:2"
```

