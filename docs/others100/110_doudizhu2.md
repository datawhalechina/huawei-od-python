#  110-斗地主（2），斗地主之顺子

## 题目描述

在斗地主扑克牌游戏中，扑克牌由小到大的顺序为 `3 4 5 6 7 8 9 10 J Q K A 2`
玩家可以出的扑克牌阵型有， `单张`， `对子`， `顺子` ，`飞机`， `炸弹` 等
其中顺子的出牌规则为，由至少 5 张由小到大连续递增的扑克牌组成且不能包含 `2`
例如: `{3,4,5,6,7}` 、`{3,4,5,6,7,8,9,10,J,Q,K,A}` 都是有效的顺子
而`{J,Q,K,A,2}`、`{2,3,4,5,6}`、 `{3,4,5,6}`、`{3,4,5,6,8}`等都不是顺子
给定一个包含 `13` 张牌的数组，如果有满足出牌规则的顺子，请输出顺子
如果存在多个顺子，请每行输出一个顺子,且需要按照顺子的第一张牌的大小(必须从小到大)依次输出
如果没有满足出牌规则的顺子，请输出 `No`

## 输入描述

13 张任意顺序的扑克牌，每张扑克牌数字用空格隔开，每张扑克牌的数字都是合法的,并且不包括大小王:`2 9 J 3 4 K A 7 9 A 5 6`
不需要考虑输入为异常字符的情况

## 输出描述

组成的顺子 每张扑克牌数字用空格隔开 `3 4 5 6 7`

## 示例描述

### 示例一

**输入：**

```text
2 9 J 2 3 4 K A 7 9 A 5 6
```

**输出：**

```text
3 4 5 6 7
```

**说明：**  

`13` 张牌中可以组成的顺子只有一组: `3 4 5 6 7`

### 示例二

**输入：**

```text
2 9 J 10 3 4 K A 7 Q A 5 6
```

**输出：**

```text
3 4 5 6 7
9 10 J Q K A
```

**说明：**  

`13` 张牌中可以组成两组顺子，从小到大分别为:
 `3 4 5 6 7`
`9 10 J Q K A`

### 示例三

**输入：**

```text
2 9 9 9 3 4 K A 10 Q A 5 6
```

**输出：**

```text
No
```

**说明：**  

`13` 张牌中无法组成顺子

## 解题思路

1. 忽略输入字符串中的"2",将输入的牌分成各个子列表`sub_checklist`，每个列表按牌面大小升序排列，且没有重复的牌。
2. `sub_checklist`组成一个大的`checklist` ,遍历`checklist`用`find`函数找出所有可能顺子返回结果。

`find函数`

1. 搜索输入的牌列不连续的位置，并加入到`cut_point`列表中，通过`cut_point`列表我们可以找连续的牌段，以及他们的长度。
2. 检测每个牌段是否足够有5张，如果有返回顺子。

## 解题代码

```python
graph = ["3","4","5","6","7","8","9","10","J","Q","K", "A"]
#给牌按顺序标记 以便于后面找连续的牌
graph_num={}
for i in range(len(graph)):
	graph_num[graph[i]] = i
def find(graph_rest): 
	#记录不连续的位置
	cut_point=[-1]
	for i in range(len(graph_rest)-1):
		if  graph_num[graph_rest[i+1]]-graph_num[graph_rest[i]]>1:
			cut_point.append(i)
	res=[]
	cut_point.append(len(graph_rest)-1)
	for i  in range(1,len(cut_point)):
		l= cut_point[i]-cut_point[i-1]
		res_point1,res_point2=0,0

		if l >=5 :
			res_point1,res_point2=cut_point[i-1],cut_point[i]
			#res_point1= -1 if res_point1 ==0 else res_point1
			if res_point2!=0:
				res.append(" ".join(map(str,graph_rest[res_point1+1:res_point2+1])))

	return res


def solve_method(s):
	s=s.split(" ")
	s1=[]
	for i in graph:
		s1.append(s.count(i))
	maxcount=max(s1)
	checklist=[]
	for i in range(maxcount):
		sub_checklist=[]
		for j in  range(len(s1)):
			if s1[j] >0 :
				sub_checklist.append(graph[j])
				s1[j]-=1

		checklist.append(sub_checklist)

	result=[]
	
	for  i in checklist:
		result.extend(find(i))
	
	if len(result)==0:
		result=["No"]
	else:
		result.sort(key=lambda x :  graph_num[x[0]] if x!='10' else graph_num['10'])
	return result


if __name__ == "__main__":
	
	assert solve_method("2 9 J 10 3 4 K A 7 Q A 5 6") == ['3 4 5 6 7', '9 10 J Q K A']
	assert solve_method("2 9 J 2 3 4 K A 7 9 A 5 6") == ['3 4 5 6 7']
	assert solve_method("2 9 9 9 3 4 K A 10 Q A 5 6") == ['No']
```

