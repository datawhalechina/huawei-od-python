#  109-斗地主

## 题目描述

斗地主起源于湖北十堰房县，
据传是一位叫吴修全的年轻人根据当地流行的扑克玩法“跑得快”改编的，
如今已风靡整个中国，并流行于互联网上。

牌型:
单顺，又称顺子，最少 `5` 张牌，最多 `12` 张牌( `3...A` ),不能有 `2`，
也不能有大小王，不计花色
例如: `3-4-5-7-8`， `7-8-9-10-J-0`， `3-4-5-6-7-8-9-10-J-0-K-A`
可用的牌 `3<4<5<6<7<8<9<10<J<Q<K<A<2<B(小王)<C(大王)`,
每种牌除大小王外有 `4` 种花色(共有 `13X4+2` 张牌)

输入：

1. 手上已有的牌
2. 已经出过的牌(包括对手出的和自己出的牌)

输出:

对手可能构成的最长的顺子(如果有相同长度的顺子，输出牌面最大的那一个)，如果无法构成顺子，则输出 `NO-CHAIN`

## 输入描述

输入的第一行为当前手中的牌
输入的第一行为已经出过的牌

## 输出描述

最长的顺子

## 示例描述

### 示例一

**输入：**

```
3-3-3-3-4-4-5-5-6-7-8-9-10-J-Q-K-A
4-5-6-7-8-8-8
```

**输出：**

```
9-10-J-Q-K-A
```

### 示例二

**输入：**

```
3-3-3-3-8-8-8-8
K-K-K-K
```

**输出：**

```
NO-CHAIN
```

## 解题思路

- 本题目标实现一个找扑克牌Q顺子的功能，扑克牌包含了 ["3","4","5","6","7","8","9","10","J","Q","K", "A"]这 12 张牌。
- solveMethod 函数:这是要的函数，它首先通过 diff 函数外理手和对手，将其中的牌从"cards"字典中减去。然后通过 find函数，在剩余的牌中找到顺子，如果找到了就返回字符串形式的顺子，否则返回"NO-CHAIN”。

## 解题代码

```python
graph = ["3","4","5","6","7","8","9","10","J","Q","K", "A"]
cards = {}
for card in graph:
	cards[card] = 4

def solveMethod(my, over):
	diff(cards, my)
	diff(cards, over)
	#print(cards)
	res = find(cards)
	print(res)


def diff(cards,string):
	for card in string.split("-"):
		if card in cards:
			cards[card] -= 1


def find(cards):
	res = "NO-CHAIN"

	l, r = 0 , 0 
	for i in range(0, len(graph)):
		card = graph[i]
		if cards[card] > 0:
				l = i
				while  i < len(graph) - 1 and cards[graph[i + 1]] > 0:
					i += 1

				r = i + 1

				if r - l > 5:
					res = "-".join(graph[l:r])


	return res

my = input()
over = input()
solveMethod(my,over)


```