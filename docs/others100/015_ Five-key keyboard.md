# 015-五键键盘

## 题目描述

有一个特殊的五键键盘
上面有A、Ctrl-C、Ctrl-X、Ctrl-V、Ctrl-A
A键在屏幕上输出一个字母A
Ctrl-c将当前所选的字母复制到剪贴板
Ctrl-X将当前选择的字母复制到剪贴板并清空所选择的字母
Ctrl-V将当前剪贴板的字母输出到屏幕
Ctrl -A选择当前屏幕中所有字母
注意：

1. 剪贴板初始为空
2. 新的内容复制到剪贴板会覆盖原有内容
3. 当屏幕中没有字母时，Ctrl-A无效
4. 当没有选择字母时Ctrl-c、Ctrl-X无效
5. 当有字母被选择时A和Ctrl-V这两个输出功能的键，
   会先清空所选的字母再进行输出

给定一系列键盘输入，
输出最终屏幕上字母的数量

## 输入描述

输入为一行
为简化解析用数字12345分别代替A、Ctrl-C、Ctrl-X、Ctrl-V、Ctrl-A的输入
数字用空格分割

## 输出描述

输出一个数字为屏幕上字母的总数量

## 示例描述

### 示例一

**输入：**
```
1 1 1
```

**输出：**
```
3
```

## 解题思路

* 输入一行数字，将其存储为字符串nums。
* 将nums按空格分割成字符串列表nums_list。
* 声明一个字符串builder用于存储构建的字符串，以及两个字符串select和copy用于辅助操作。
* 遍历nums_list,根据数字执行不同的操作。
* 若数字为1，将builder字符串中的select部分清空，然后在builder字符串末尾添加字符A。
* 若数字为2，如果select字符串不为空，将select字符串赋值给copy字符串。
* 若数字为3，如果select字符串不为空，则将select字符串赋值给copy字符串，然后清空select字符串和builder字符串
* 若数字为4，将builder字符串中的select部分清空，然后将copy字符串添加到builder字符串末尾。
* 若数字为5，如果builder字符串不为空，则将builder字符串赋值给select字符串。
* 最后输出builder字符串的长度。

## 解题代码

```python
def solve_method(nums):
    # 将输入的数字字符串分割成列表
    nums_list = nums.split(" ")
    # 初始化变量 builder、select 和 copy
    builder = ""
    select = ""
    copy = ""
    # 遍历数字列表
    for op in nums_list:
        if op == "1":
            # 执行操作1：清空 select，并在 builder 中添加 'A'
            select = empty(builder, select)
            builder += 'A'
        elif op == "2":
            # 执行操作2：复制 select 的值给 copy
            if select != "":
                copy = select
        elif op == "3":
            # 执行操作3：清空 select、builder 和 copy 的值
            if select != "":
                copy = select
                select = ""
                builder = ""
        elif op == "4":
            # 执行操作4：清空 select，并在 builder 中添加 copy 的值
            select = empty(builder, select)
            builder += copy
        elif op == "5":
            # 执行操作5：将 builder 的值赋给 select
            if len(builder) != 0:
                select = builder
        else:
            pass
    # 输出 builder 的长度
    print(len(builder))

def empty(builder, select):
    # 清空 select 在 builder 中的值，并将 select 置为空字符串
    if select != "":
        builder = builder.replace(select, "")
        select = ""
    return select

def main():
    # 读取输入的数字字符串，调用 solve_method 函数进行处理
    nums = input()
    solve_method(nums)

if __name__ == '__main__':
    main()
```

