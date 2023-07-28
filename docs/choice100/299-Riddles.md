# 299 猜字谜

## 题目描述
小王设计了一个简单的猜字谜游戏，游戏的谜面是一个错误的单词，比如nesw，玩家需要猜出谜底库中正确的单词。
猜中的要求如下：
对于某个谜面和谜底单词，满足下面任一条件都表示猜中：

1. 变换顺序以后一样的，比如通过变换w和e的顺序，nwes跟news是可以完全对应的；
2. 字母去重以后是一样的，比如woood和wood是一样的，它们去重后都是wod

请你写一个程序帮忙在谜底库中找到正确的谜底。 \
谜面是多个单词，都需要找到对应的谜底，如果找不到的话，返回not found
## 输入描述
1. 谜面单词列表，以,分隔
2. 谜底库单词列表，以,分隔
3. 单词的数量N的范围：$0<N<1000$ 
4. 词汇表的数量M的范围： $0<M<1000$
5. 单词的长度P的范围：$0<P<20$ 
6. 输入的字符只有小写英文字母，没有其它字符
## 输出描述
匹配到的正确单词列表，以,分隔
如果找不到，返回not found
### 示例一
**输入：**
```shell
conection
connection,today
```

**输出：**
```shell
connection
```

**说明：**  

### 示例二
**输入：**
```shell
bdni,wooood
bind,wrong,wood
```

**输出：**
```shell
bind,wood
```

**说明：**  

## 解题思路
将需要检查的字符串和目标字符串去重并排序，比较是否相等，全部都不相等则输出not found

## 解题代码

```python
# 输入获取
issues = input().split(",")
answers = input().split(",")
 
 
# 算法入口
def getResult(issues, answers):
    ans = []
 
    for issue in issues:
        str1 = "".join(sorted(set(issue)))
        find = False
 
        for answer in answers:
            str2 = "".join(sorted(set(answer)))
 
            if str1 == str2:
                ans.append(answer)
                find = True
                # break # 如果一个谜面对应多个谜底，这里就不能break，如果一个谜面只对应一个谜底，那这里就要break，考试的时候都试下
 
        if not find:
            ans.append("not found")
 
    return ",".join(ans)
 
 
# 算法调用
print(getResult(issues, answers))
```