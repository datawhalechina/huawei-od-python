# 009-We Are A Team

## 题目描述

总共有n个人在机房，每个人有一个标号(1<=标号<=)，他们分成了多个团队，需要你根据收到的m条消息判定指定的两个人是否在
一个团队中，具体的：

1. 消息构成为abc,整数a、b分别代表两个人的标号，整数c代表指令
2. c==0代表a和b在一个团队内
3. c==1代表需要判定a和b的关系，如果a和b是一个团队，输出一行we are a team',如果不是，输出一行we are not a team
4. c为其他值，或当前行a或b超出1~n的范围，输出da pian z”

## 输入描述

* 第一行包含两个整数n,m(1<=n,m<100000),分别表示有n个人和m条消息
* 随后的m行，每行一条消息，消息格式为：abc(1<=a,b<=n,0<=c<=1)

## 输出描述

## 示例描述

### 示例一

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

1. 输入两个整数n和m,表示有n个人和m条关系；
2. 依次读入m条关系，每条关系由三个整数X、y、relation组成，表示第X个人和第y个人的关系是relation;
3. 将关系分为两类：已确定的关系和待验证的关系。已确定的关系包括relation=0的关系，待验证的关系包括relation=1的关系；
4. 对于已确定的关系，将其添加到关系集合中，其中每个集合包含有关系的所有人，即每个集合代表了一个团队：
5. 对于待验证的关系，如果关系为0，则跳过；如果关系为1，检查这两个人是否在同一个团队中，如果是，则输出"we are a team",
   否则输出"we are not a team"。

## 解题代码

```python
# coding:utf-8
import sys
# 读取输入一行并分割转换为整数赋值给n，m
n,m = map(int,sys.stdin.readline().split())
# 关系集合
relationship_sets = []
# 待验证的关系
verify_relationships = []
# 读取m行
for i in range(m):
    relationship = sys.stdin.readline().strip().split()
    # 逐个赋值
    x,y,relation = map(int,relationship)
    # 不等于0证明要验证
    if relation != 0:
        verify_relationships.append(relationship)
    else:
        set_added = False
        for j in range(len(relationship_sets)):
            # 取出关系集合中的每个set
            set_ = relationship_sets[j]
            # 只需要判断其中一个是否在其中
            if x in set_ or y in set_:
                # 加入该集合
                set_.add(x)
                set_.add(y)
                set_added = True
                break
        # 不存在则另外创建新的集合并把xy存入
        if not set_added:
            new_set = set()
            new_set.add(x)
            new_set.add(y)
            relationship_sets.append(new_set)
 # 处理待验证的集合
for i in range(len(verify_relationships)):
    relationship = verify_relationships[i]
    x,y,relation = map(int,relationship)
    if relation != 1:
        print("da pian zi")
        continue
    is_team = False
    for j in range(len(relationship_sets)):
        set_=relationship_sets[j]
        if x in set_ and y in set_:
            print("we are a team")
            is_team = True
            break
    if not is_team:
        print("we are not a team")
```

