#  119-最大排列

## 题目描述

给定一组整数，重排序后输出一个最大的整数

## 输入描述

数字组合

## 输出描述

最大的整数

## 示例描述

### 示例一

**输入：**

```text
10 9
```

**输出：**

```text
910
```

## 解题思路

对输入`nums`按字符串大小的特性逆序排序即可。

## 解题代码

```python
def solve_method(nums):
	nums=nums.split(" ")
	nums.sort(reverse=True)
	

	return "".join (nums)

if __name__ == '__main__':

	assert solve_method("10 9") == '910'
```



