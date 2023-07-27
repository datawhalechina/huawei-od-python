#  109-斗地主

## 题目描述

斗地主起源于湖北十堰房县，
据传是一位叫吴修全的年轻人根据当地流行的扑克玩法“跑得快”改编的，
如今已风靡整个中国，并流行于互联网上。

牌型:
单顺，又称顺子，最少 5 张牌，最多 12 张牌( 3...A ),不能有 2，
也不能有大小王，不计花色
例如: `3-4-5-7-8`， `7-8-9-10-J-Q`， `3-4-5-6-7-8-9-10-J-Q-K-A`
可用的牌 `3<4<5<6<7<8<9<10<J<Q<K<A<2<B(小王)<C(大王)`,
每种牌除大小王外有 4 种花色(共有 `13X4+2` 张牌)



## 输入描述

输入的第一行为当前手中的牌
输入的第二行为已经出过的牌(包括对手出的和自己出的牌)

## 输出描述

对手可能构成的最长的顺子(如果有相同长度的顺子，输出牌面最大的那一个)，如果无法构成顺子，则输出 `NO-CHAIN`

## 示例描述

### 示例一

**输入：**

```text
3-3-3-3-4-4-5-5-6-7-8-9-10-J-Q-K-A
4-5-6-7-8-8-8
```

**输出：**

```text
9-10-J-Q-K-A
```

### 示例二

**输入：**

```text
3-3-3-3-8-8-8-8
K-K-K-K
```

**输出：**

```text
NO-CHAIN
```

## 解题思路



1. 创建一个graph_num字典，给牌按顺序标记 以便于后面找连续的牌。
2. 初始化一个cards字典，包含游戏开始每张牌的数目。
3. 删去自己的牌和已经打掉的牌，构建一个grap_rest数组记录对手还有哪几种牌在手上。
4. 然后通过 find函数，搜索剩余的牌不连续的位置，并加入到为cut_point列表中，通过cut_point列表我们可以找连续的牌段，以及他们的长度。
5. 检测每个牌段是否足够有5张，如果没有返回`"NO-CHAIN"`，如果有返回最长且最大的牌。

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

	cut_point.append(len(graph_rest)-1)
	for i  in range(1,len(cut_point)):
		l= cut_point[i]-cut_point[i-1]
		res_point1,res_point2=0,0

		if l >=5 and l > (res_point2-res_point1):
			res_point1,res_point2=cut_point[i-1],cut_point[i]

	
	res="NO-CHAIN" if res_point2==0 else "-".join(map(str,graph_rest[res_point1+1:res_point2+1]))

	return res


def solve_method(my, over):

	cards = {}
	for card in graph:
		cards[card] = 4
	for card in (my+"-"+over).split("-"):
		if card in cards:
			cards[card] -= 1
			if cards[card] == 0:
				 del cards[card]
	graph_rest=list(cards.keys())
	
	return find(graph_rest)



if __name__ == "__main__":
	my,over="3-3-3-3-4-4-5-5-6-7-8-9-10-J-Q-K-A","4-5-6-7-8-8-8"
	assert solve_method(my,over) == "9-10-J-Q-K-A" 
	my,over="3-3-3-3-4-4-5-5-6-7-8-9-10-J-Q-K-A","4-5-6-7-8-8-8"
	assert solve_method(my,over) == "9-10-J-Q-K-A" 
	my,over="3-3-3-3-8-8-8-8","K-K-K-K"
	assert solve_method(my,over) == "NO-CHAIN" 
	my,over="3-8","K-K"
	assert solve_method(my,over) == "3-4-5-6-7-8-9-10-J-Q-K-A"

```