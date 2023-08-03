# 038 剩余可用字符集

## 题目描述

给定两个字符集合
一个是全量字符集
一个是已占用字符集
已占用字符集中的字符不能再使用
要求输出剩余可用字符集

## 输入描述

1. 输入一个字符串 一定包含 `@` 
`@`前为全量字符集 `@` 后的为已占用字符集

2. 已占用字符集中的字符
一定是全量字符集中的字符
字符集中的字符跟字符之间使用 `英文逗号` 隔开

3. 每个字符都表示为字符+数字的形式
用英文冒号分隔
比如 `a:1`表示一个  `a` 字符

4. 字符只考虑英文字母，区分大小写数字只考虑正整型 不超过 100

5. 如果一个字符都没被占用 `@` 标识仍存在
例如 `a:3,b:5,c:2@`

## 输出描述

输出可用字符集
不同的输出字符集之间用回车换行
注意： 输出的字符顺序要跟输入的一致
不能输出 `b:3,a:2,c:2`
如果某个字符已全部占用 则不需要再输出

## 示例描述

### 示例一

**输入：**

```Plain Text
a:3,b:5,c:2@a:1, b:2
```

**输出：**

```Plain Text
a:2,b:3,c:2
```

**说明：**
全量字符集为`3个a`，`5个b`，`2个c`
已占用字符集为 `1个 a`，`2个 b`
由于已占用字符不能再使用
因此剩余可用字符为`2个 a`，`3 个 b`，`2个c`
因此输出 `a:2,b:3,c:2`

## 解题思路

基本思路：

1. `input().split("@")` 将输入字符串按照 "@" 进行分割，并将结果分别赋值给 `total` 和 `used`。

2. 分别遍历`total`和`used`，对每对键值进行拆分，存于`total_map`和`used_map`，将每对第二个元素转为整数类型便于计算

3. 遍历`used_map`中的键，并与`total_map`相对于的键进行计算求出剩余量`diff`。如果`diff>0`则更新值，如果小于或等于0，则删除键

4. 返回结果

## 解题代码

```Python
def solve(n,m):
    # 拆分键值并保存
    def x_map(n):
        x_map = {}
        for i, j in list(map(lambda x: x.split(":"), n.split(","))):
            x_map[i] = int(j)
        return x_map
    
    
    total_map = x_map(total)
    used_map = x_map(used)
    for i in used_map.keys():
        diff = total_map[i] - used_map[i]
        if diff > 0:
            total_map[i] = diff
        else:
            total_map.pop(i)
    return (",".join(map(lambda x: ":".join(map(str, x)), total_map.items())))
if __name__ == '__main__':
    total, used = input().split("@")
    result = solve(total,used)
    print(result)
```

