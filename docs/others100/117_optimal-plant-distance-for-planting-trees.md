#  117-最佳植树距离、种树问题

## 题目描述

小明在直线的公路上种树，现在给定可以种树的坑位的数量和位置，以及需要种多少棵树苗，问树苗之间的最小间距是多少时，可以保证种的最均匀(两棵树苗之间的最小间距最大)

## 输入描述

输入两行

1. 第一行以空格分隔的数组: 坑位的位置
2. 第二行一个整数:需要种植树苗的数量

## 输出描述

树苗之间的最小间距

## 示例描述

### 示例一

**输入：**

```text
1 3 6 7 8 11 13
3
```

**输出：**

```text
6
```

**说明：**  

三颗树苗分别种在 1、7、13 的位置，可以保证种的最均匀，树苗之间的最小间距为 6。

## 解题思路

二分法

1. 初始化最小间距的可能范围(上限`right`， 下限`left`)
2. 从可能范围中间mid开始检查 ，当最小间距为mid时可以种几棵树。检查方式如下：
   1. 初始化previous 为第一个坑的位置  种树数目为1 count=1
   2. 以previous 为基准 找下一个大于等于mid距离的坑的位置 ，找到后count累加 ，previous记录为现在坑的位置。
   3. 重复a-b直到最后一个坑。
3. 如果当最小间距为mid时可以栽种的树的数目大于等于 需要种植树苗的数量`target`，则把mid赋值给answer。把可能范围设置为(left,right)=(mid+1, right),以找到更大的mid。
4. 如果当最小间距为mid时可以栽种的树的数目小于 需要种植树苗的数量`target`，把可能范围设置为(left,right)=(left, mid-1),以找到更小的mid。
5. 重复2-4直到left>right 返回结果。

## 解题代码

```python
def solve_method(holes, target):
	holes.sort()
	left = 0
	right = holes[-1] - holes[0]
	answer = -1 

	while left <= right:
		mid = left + (right - left) // 2
		count =1 
		previous = holes[0]
		for i in range(1, len(holes)):
			if holes[i] - previous >= mid:
				count += 1
				previous = holes[i]

				if count >= target:
					answer = mid
					left = mid +1 
					break


		if count < target:
			right= mid - 1

	return answer



if __name__ == '__main__':

	assert solve_method([1,3,6,7,8,11,13],3) == 6
```



