# 047 叠放书籍

## 题目描述

书籍的长宽都是整数对应`(l,w)`，如果书`A`的长宽度都比`B`长宽大时，则允许将`B`排列放在`A`上面。

现在有一组规格的书籍，书籍叠放时要求书籍不能做旋转，请计算最多有多少个规格书籍能叠放在一起。

## 输入描述

输入一个数组`books`，每个元素表示书籍的长宽，例如：`[20,16],[15,11],[10,10],[9,10]`。

总共有4本书，第一本长度为20宽度为16，第二本长度为15宽度为11，以此类推，最后一本书长度为9宽度为10。

## 输出描述

最多可以叠放在一起的规格书籍的数量，输出：3。

最多三个规格的书籍可以叠放在一起，从下到上依次是`[20,16],[15,11],[10,10]`。

## 示例描述

### 示例一

**输入：**
```text
[[20,16],[15,11],[10,10],[9,10]]
```

**输出：**
```text
3
```

## 解题思路

题目同力扣354. 俄罗斯套娃信封问题。先对长度进行升序排序，如果遇到长度相同的情况，
则按照宽度降序排序。之后把所有的宽度作为一个数组，在这个数组上计算LIS的长度就是答案。
这个解法的关键在于，对于长度相同的书籍，要对其宽度进行降序排序。
因为两个长度相同的信封不能相互包含的，逆序排序保证在长度相同的书籍中最多只选取一个。

```python
def rearrange_books(nums):
    def getMaxLIS(nums):
        dp = [nums[0]]
        ans = 1
        for i in range(1, len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
                ans += 1
            else:
                l, r = 0, ans - 1
                while l <= r:
                    mid = l + (r - l) // 2
                    if dp[mid] == nums[i]:
                        l = mid
                        break
                    elif dp[mid] > nums[i]:
                        r = mid - 1
                    elif dp[mid] < nums[i]:
                        l = mid + 1
                dp[l] = nums[i]

        return ans

    nums = sorted(nums, key=lambda x: (x[0], -x[1]))
    widths = [x[1] for x in nums]

    return getMaxLIS(widths)


if __name__ == '__main__':
    nums = eval(input().strip())
    res = rearrange_books(nums)
    print(res)

```

