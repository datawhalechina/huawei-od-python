#  110-斗地主（2），斗地主之顺子

## 题目描述

在斗地主扑克牌游戏中，扑克牌由小到大的顺序为 `3 4 5 6 7 8 9 1  K A 2`
玩家可以出的扑克牌阵型有， `单张`， `对子`， `顺子` ，`飞机`， `炸弹` 等
其中顺子的出牌规则为，由至少 5 张由小到大连续递增的扑克牌组成且不能包含 `2`

例如: `{3,4,5,6,7}` 、`{3,4,5,6,7,8,9,10,J,Q,K,A}` 都是有效的顺子

而`{J,Q,K,A,2}`、`{2,3,4,5,6}`、 `{3,4,5,6}`、`{3,4,5,6,8}`等都不是顺子

给定一个包含 `13` 张牌的数组，如果有满足出牌规则的顺子，请输出顺子

如果存在多个顺子，请每行输出一个顺子

且需要按照顺子的第一张牌的大小(必须从小到大)依次输出

如果没有满足出牌规则的顺子，请输出 `No`

## 输入描述

13 张任意顺序的扑克牌，每张扑克牌数字用空格隔开，每张扑克牌的数字都是合法的
并且不包括大小王:`2 9 2 3 4 K A7 9 A 5 6`
不需要考虑输入为异常字符的情况

## 输出描述

组成的顺子 每张扑克牌数字用空格隔开 `3 4 5 6 7`

## 示例描述

### 示例一

**输入：**

```
2 9 J 2 3 4 K A 7 9 A 5 6
```

**输出：**

```
3 4 5 6 7
```

**说明：**  

`13` 张牌中可以组成的顺子只有一组: `3 4 5 6 7`

### 示例二

**输入：**

```
2 9 J 10 3 4 K A 7 Q A 5 6
```

**输出：**

```
3 4 5 6 7
9 10 J Q K A
```

**说明：**  

`13` 张牌中可以组成两组顺子，从小到大分别为:
 `3 4 5 6 7`
`9 10 J Q K A`

### 示例三

**输入：**

```
2 9 9 9 3 4 K A 10 Q A 5 6
```

**输出：**

```
No
```

**说明：**  

`13` 张牌中无法组成顺子

## 解题思路



## 解题代码

```python
def solve_method():
	s = input().split(" ")

	len_s = len(s)
	list_s = []

	for i in range(len_s):
		if s[i] == "J":
			list_s.append(11)
		elif s[i] == "Q":
			list_s.append(12)
		elif s[i] =="K":
			list_s.append(13)
		elif s[i] =="A":
			list_s.append(14)
		elif s[i] != "2":
			list_s.append(int(s[i]))


	list_s.sort()


	ress = []
	is_a = False

	while not is_a:
		res = [list_s[0]]
		count = 1

		for i in range(1, len(list_s)):
			x = list_s[i]

			if x == list_s[i - 1] + 1 :
				count += 1
				res.append(x)
			elif x == list_s[i - 1] and i != len(list_s) - 1:
				continue

			if x != list_s[i-1] + 1 or i == len(list_s) - 1:
				if count >= 5:
					ress.append(res)
				elif i == len(list_s) -1 :
					is_a = True
					break

				for j in range(len(res)):
					for k in range(len(list_s)):
						if res[j] == list_s[k]:
							list_s.pop(k)
							break


				if len(list_s) < 5 :
					is_a = True


				break


	if len(ress) == 0:
		print("No")
	else:
		for i in range(len(ress)):
			string_res = " "
			for j in range(len(ress[i])):
				if ress[i][j] == 11:
					string_res += "J"
				elif ress[i][j] == 12:
					string_res += "Q"
				elif ress[i][j] == 13:
					string_res += "K"
				elif ress[i][j] == 14:
					string_res += "A"
				else:
					string_res += str(ress[i][j])
				

				if i < len(ress[i]) - 1:
					string_res += " "

			print(string_res)


if __name__ == "__main__":
	solve_method()
```

## 代码运行结果

```
2 9 J 2 3 4 K A 7 9 A 5 6
3 4 5 6 7
```

