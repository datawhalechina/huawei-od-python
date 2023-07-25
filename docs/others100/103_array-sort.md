#  103 数组排序

## 题目描述

给定一个乱序的数组，删除所有重复元素，使得每个元素只出现一次，并且按照出现的次数从高到低进行排序，相同出现次数按照第一次出现顺序进行先后排序。其中，数组大小不超过100，数组元素值不超过100。

## 输入描述

一个数组。

## 输出描述

去重排序后的数组。

## 示例描述

### 示例一

**输入：**

```text
1,3,3,3,2,4,4,4,5
```

**输出：**

```text
3,4,1,2,5
```

## 解题思路

- 解析输入的字符串，将其以，为分隔符分割为多个数字。
- 将每一个数字记录到列表 list 中，并统计每个数字出现的次数，记录到字典 map 中。
- 将 list 中的数字及其出现次数记录为二元组，并存入结果列表 res 中

## 解题代码

```python
def solve_method(line):
	split = line.split(",")
	list = []
	map = {}
	for item in split:
		num = int(item)
		if num not in list:
			list.append(num)
		if num in map:
			map[num] += 1
		else:
			map[num] = 1


	res = []
	for i in list:
		ints = [i, map[i]]
		res.append(ints)

	res.sort(key=lambda x: x[1], reverse=True)

	result = []
	for i in range(len(res)):
		result.append(str(res[i][0]))

	print(",".join(result))
```
