#  101-数据最节约的备份方法

## 题目描述

有若干个文件，使用刻录光盘的方式进行备份，假设每张光盘的容量是500MB，求使用的光盘最少的文件分布方式 。

所有文件的大小都是整数的MB,且不超过500MB；文件不能分割、分卷打包。

## 输入描述

一组文件大小的数据

## 输出描述

使用光盘的数量

## 补充说明

不用考虑输入数据不合法的情况；假设最多100 个输入文件。

## 示例描述

### 示例一

**输入：**

```
100，500，300，200，400
```

**输出：**

```
3
```

**说明：**  

(100,400),(200,300),(500) 3张光盘即可。

输入和输出内容都不含空格。

### 示例二

**输入：**

```
100,100,200,300
```

**输出：**

```
2
```

## 解题思路

通过二分查找的方式确定能够满足文件分配条件的最小光盘数量。（解法一）

通过递归的方法求解（解法二）

1. 初始化 建立一个排序过的光盘列表`arr`  取`num=0`
2. 将输入光盘列表中光盘容量值最大和最小的相加
3. 比较相加结果：
   1.  如果刚好等于500 在光盘列表中删除最大和最小容量光盘 对所需容量加1；
   2. 如果大于500 则在光盘列表中删除最大容量光盘，在光盘列表中删除最大；
   3. 如果小于500 则把相加值赋给光盘列表中最大容量光盘，再删除光盘列表中最小容量光盘。
4. 检查列表长度
   1. 如果列表长度小于等于1则返回最小光盘数量为`num+len(arr)`（现在光盘列表长度）
   2. 如果列表长度大于1重复2-3步

## 解题代码

### 解法一

```python
def can_allocate(files, num_boxes):
	#创建一个长度为num_boxes的光盘列表，初始值为500
	box_capacities = [500] * num_boxes
	
	#文件列表中的最后一个文件开始分配
	for file in reversed(files):
		#对光盘容量进行排序，确保每次选择容量最小的箱子进行分配
		box_capacities.sort()

		#检查最大容量的光盘是否能够容纳当前文件
		if box_capacities[num_boxes - 1] >= file:
			box_capacities[num_boxes - 1] -= file
		else:
			#如果最大容量的光盘无法容纳当前文件，则无法完成分配
			return False


	#如果能够成功分配所有文件，则返回True
	return True

def solve_method():
	#分隔的文件列表 并转换为整数数组
	files = list(map(int, input().split(",")))
	files.sort() # 对文件列表进行排序

	min_boxes = 0
	max_boxes = len(files) + 1

	#使用二分查找确定最小的光盘数量
	while min_boxes < max_boxes:
		mid = (min_boxes + max_boxes) // 2
		if can_allocate(files, mid):
			#如果能够完成分配，则缩小光盘数量的上限
			max_boxes = mid
		else:
			#如果无法完成分配，则增加光盘数量的下限
			min_boxes = mid + 1

	print(min_boxes)
if __name__ == "__main__":
	solve_method()
```

### 解法二

```python
def solve_method(arr, num):
	if len(arr) <=1:
		print(num+len(arr))
		return num+len(arr)
	else:
		if arr[0]+arr[-1]<500:
			arr[-1]+=arr[0]
			arr.pop(0)
		else:
			if arr[0]+arr[-1]==500:
				arr.pop()
				arr.pop(0)
			else:
				arr.pop()
			num+=1
		solve_method(arr,num)

if __name__ == "__main__":
	files = list(map(int, input().split(",")))
	files.sort()
	solve_method(files,0)
```

