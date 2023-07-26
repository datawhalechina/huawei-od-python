# 008 We Are A Team

## 题目描述

总共有`n`个人在机房，每个人有一个标号（1 <= 标号 <= n），他们分成了多个团队，需要你根据收到的`m`条消息判定指定的两个人是否在一个团队中，具体的规则如下：

- 消息构成为`a b c`，整数`a`、`b`分别代表两个人的标号，整数`c`代表指令。
- `c==0`代表`a`和`b`在一个团队内。
- `c==1`代表需要判定`a`和`b`的关系，如果`a`和`b`是一个团队，输出一行`we are a team`，如果不是，输出一行`we are not a team`。
- `c`为其他值，或当前行`a`或`b`超出1\~n的范围，输出`da pian zi`。

## 输入描述

第1行包含两个整数`n`、`m`（1 <= n,m < 100000），分别表示有`n`个人和`m`条消息。

随后的`m`行，每行一条消息，消息格式为：`a b c`（1 <= a,b <= n， 0 <= c <=1）。

## 输出描述

- 如果`c==0`，代表`a`和`b`在一个团队内。
- 如果`c==1`，需要判定`a`和`b`的关系，如果`a`和`b`是一个团队，输出一行`we are a team`，如果不是，输出一行`we are not a team`。
- 如果`c`为其他值，或当前行`a`或`b`超出1\~n的范围，输出`da pian zi`。
- 如果第1行`n`和`m`的值超出约定的范围时，输出字符串`NULL`。

## 示例描述

### 示例一

**输入：**
```text
5 7
1 2 0
4 5 0
2 3 0
1 2 1
2 3 1
4 5 1
1 5 1
```

**输出：**
```text
We are a team
We are a team
We are a team
We are not a team
```

### 示例二

**输入：**
```
5 6
1 2 0
1 2 1
1 5 0
2 3 1
2 5 1
1 3 2
```

**输出：**
```
we are a team
we are not a team
we are a team
da pian zi
```

## 解题思路

1. 初始化团队列表，每个团队都是一个set集合。
2. 如果c为其他值，或当前行a或b超出1\~n的范围，则将`da pian zi`存入结果列表中。
3. 如果c为0，添加到对应的团队中的set集合。
4. 如果c为1，判断a和b是否在一个团队。
   - 如果在，将`We are a team`存入结果列表中。
   - 如果不在，将`We are not a team`存入结果列表中。

## 解题代码

```python
def solve_method(n, messages):
    result = []
    # 团队列表，每个团队都是一个set集合
    relations = []
    for message in messages:
        # 如果c为其他值，或当前行a或b超出1\~n的范围，输出da pian zi。
        if message[2] not in [0, 1] or message[0] > n or message[1] > n:
            result.append("da pian zi")
        else:
            if message[2] == 0:
                # 如果c为0，添加到对应的团队中
                set_added = False
                for relation in relations:
                    if message[0] in relation or message[1] in relation:
                        relation.add(message[0])
                        relation.add(message[1])
                        set_added = True
                        break
                if not set_added:
                    relations.append({message[0], message[1]})
            if message[2] == 1:
                # 如果c为1，判断a和b是否在一个团队
                is_team = False
                for relation in relations:
                    if message[0] in relation and message[1] in relation:
                        result.append("We are a team")
                        is_team = True
                        break
                
                if not is_team:
                    result.append("We are not a team")

    return result

if __name__ == '__main__':
    messages = [[1, 2, 0],
                [4, 5, 0],
                [2, 3, 0],
                [1, 2, 1],
                [2, 3, 1],
                [4, 5, 1],
                [1, 5, 1]]
    assert solve_method(5, messages) == ["We are a team", "We are a team",
                                         "We are a team", "We are not a team"]

    messages = [[1, 2, 0],
                [1, 2, 1],
                [1, 5, 0],
                [2, 3, 1],
                [2, 5, 1],
                [1, 3, 2]]
    assert solve_method(5, messages) == ["We are a team", "We are not a team",
                                         "We are a team", "da pian zi"]
```
