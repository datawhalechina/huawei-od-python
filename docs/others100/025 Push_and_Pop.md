# 025 入栈出栈

## 题目描述

向一个空栈中依次存入正整数
假设入栈元素 `N(1 <= N <= 2^31-1)`
按顺序依次为 `Nx ... N4、N3、N2、N1,`
当元素入栈时，如果 `N1=N2+...Ny (y的范围[2,x],1 <= x <= 1000)`
则 `N1` 到 `Ny` 全部元素出,重新入栈新元素 `M(M=2*N1)`*
如依次向栈存储 `6、1、2、3` ,当存储 `6、1、2` 时栈底至栈顶以此为 `[6、1、2]`；
当存入 `3` 时，`3=2+1` ，`3、2、1` 全部出栈，重新入栈元素 `6`，`(6=2*3)` 此时栈中有元素 `6` 因为 `6=6`,所有两个六全部出栈存入 `12`最终栈中只剩一个元素 `12`

## 输入描述

使用单个空格隔开的正整数的字符串
如: `5 6 7 8`,左边的数字先入栈
输入的正整数个数为 `x`
`1 <= x <= 1000`

## 输出描述

最终栈中存留的元素值，元素值使用空格隔开
如 `8 7 6 5`，栈数字在左边

## 示例描述

### 示例一

**输入：**

```Plain Text
5 10 20 50 85 1
```

**输出：**

```Plain Text
1 170
```

**说明：**
5+10+20+50=85
输入85时，5、10、20、50、85全部出栈
入栈170
最终依次出栈的数字为 1 和 170

## 解题思路

**基本思路：** 参考题解，想不到好点的方法

1. 读取输入的一行数字字符串并用空格分割成多个数字字符串;

2. 将每个数字字符串转换为整数并存储在列表中;

3. 使用 while 循环，当列表长度不为 1 时循环，循环内部用 for 循环遍历列表中的每一个数字:

4. 判断前面的数字的总和是否等于当前数字，如果等于，将前面的数字删除，并在前面插入2倍的当前数字，循环结束

5. 如果前面的数字的总和大于当前数字或者遍历到列表头部，退出循环:

## 解题代码

```Python
def solve_method(line):
    strings = line.split(" ")
    nums = []
    for string in strings:
        nums.append(int(string))
    is_change = True
    while len(nums) != 1 and is_change:
        for i in range(1, len(nums)):
            n = i
            num = nums[i]
            is_end = False
            count = 0
            while not is_end:
                n -= 1
                count += nums[n]
                if count == num:
                    if i >= n:
                        del nums[n:i + 1]
                    nums.insert(n, 2 * num)
                    is_change = True
                    break
                if count > num or n == 0:
                    is_end = True
                    is_change = False
            if is_change:
                break

    res = ""
    for i in range(len(nums) - 1, -1, -1):
        res += str(nums[i])
        if i != 0:
            res += " "

    print(res)


if __name__ == '__main__':
    line = input("请输入一组数字，以空格分隔: ").strip()
    solve_method(line)
    
```

