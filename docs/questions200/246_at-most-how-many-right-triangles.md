# 246 最多几个直角三角形

## 题目描述

有 N 条线段，长度分别为`a[1]-a[N]`。

现要求你计算这 N 条线段最多可以组合成几个直角三角形，每条线段只能使用一次，每个三角形包含三条线段。

## 输入描述
第一行输入一个正整数T `(1＜= T＜= 100)`，表示有T组测试数据。

对于每组测试数据，接下来有T行，每行第一个正整数N，表示线段个数`(3<＝N＜20)`，接着是N个正整数，表示每条线段长度`0＜a[i]＜100`

## 输出描述

对于每组测试数据输出一行，每行包括一个整数，表示最多能组合的直角三角形个数。

## 示例描述

### 示例一

**输入：**
```text
1
7 3 4 5 6 5 12 13
```

**输出：**
```text
2
```

**说明：**
可以组成2个直角三角形（3，4，5）、（5，12，13）。

### 示例二

**输入：**
```text
1
7 3 4 5 6 6 12 13
```

**输出：**
```text
1
```

**说明：**
可以组成1个直角三角形（3，4，5）或（5，12，13），5只能使用一次，所以只有1个。

## 解题思路

**基本思路：**

直角三角形满足表达式a^2 + b^2 = c^2。求解满足条件的一组值时，类似3Sum，外层循环O(n)，内层循环双指针。

因为题目要求尽可能多的组合，且每条线段只能使用一次。借助visited数组和DFS。

**代码思路：**
1. 外层循环遍历c的取值
2. 内层双指针获取满足条件的a和b的取值
    - 若nums[左] + nums[右] ＜ nums[c]，左指针++；反之，右指针--
3. 借助visited数组和DFS遍，遍历所有可能的情况。

## 解题代码
```python
def solve_method(N, nums, visited):
    count = 0
    for k in range(2, N):
        c = nums[k]
        # 排除遍历过的数字
        if visited[k] == 1:
            continue

        i = 0; j = k - 1;
        while i < j:
            # 排除遍历过的数字
            while i < j and visited[i] == 1:
                i += 1
            while i < j and visited[j] == 1:
                j -= 1
            if i == j:
                break

            if nums[i] ** 2 + nums[j] ** 2 < c ** 2:
                i += 1
            elif nums[i] ** 2 + nums[j] ** 2 > c ** 2:
                j -= 1
            else:
                visited[i] = visited[j] = visited[k] = 1
                count = 1 + solve_method(N, nums, visited)
                visited[i] = visited[j] = visited[k] = 0
                break
    return count

if __name__ == "__main__":
    # 1
    # 7 3 4 5 6 5 12 13
    # 7 3 4 5 6 6 12 13
    T = int(input())
    for _ in range(T):
        line = list(map(int, input().split()))
        N = line[0]
        print(solve_method(N, sorted(line[1:]), [0] * N))

    assert solve_method(7, [3, 4, 5, 6, 5, 12, 13], [0] * 7) == 2
    assert solve_method(7, [3, 4, 5, 6, 6, 12, 13], [0] * 7) == 1
```