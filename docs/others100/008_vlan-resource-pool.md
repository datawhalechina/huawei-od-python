# 008-VLAN资源池

## 题目描述

Vlan是一种为局域网Q设备进行逻辑划分的技术
为了标识不同的vLan引入了vlan id:1~4094 之间的整数

* 定义一个vlan id的资源池

* 资源池中连续的vLan用开始vLan-结束vLan表示，不连续的用单个整数表示

* 所有的vLan用英文逗号连接起来

  现有一个vLan资源池，业务需要从资源池中申请一个vLan
  需要你输出从vLan资源池中移除申请的vLan后的资源池

## 输入描述

* 第一行为字符串格式的vLan资源池
* 第二行为业务要申请的vlan
* vlan的取值范围1~4094

## 输出描述

## 示例描述

### 示例一

**输入：**
```
1-5
2
```

**输出：**
```
1，3-5
```

**说明：**  
原vlan资源池中有12345移除2后，剩下的1345按照升序排列Q的方式为1，3-5

### 示例二

**输入：**

```
5，1-3
10
```

**输出：**

```
1-3，5
```

**说明：**  
资源池中有1235，申请的资源不在资源池中，将原池升序输出为1-3,5

## 解题思路

本题编写思路是进行一个数据处理的过程，目的是将输入的字符串进行处理，然后将结果输出。

1. 首先读入两个输入，第一个是字符串，第二个是整数：

2. 对字符串进行处理，先以“，”分割为列表，然后将列表中的每个字符串进行判断，如果是一个数字，就将其加入结果集；如果是一个
   区间，则**遍历**该区间，并将每个数加入结果集；

3. 将结果集中的要求删除的数删除，然后将结果集转为列表，并对其进行排序；

4. 然后从第一个数开始，遍历列表，如果当前数比上一个数多1，则继续遍历；否则将上一个数的结束位置和开始位置记录下来，然后
   更新开始和结束的位置，继续遍历；

5. 最后将最后的结果拼接为字符串输出，如果该数字在结果列表中单独出现，则直接输出该数字，如果是一个区间，则输出“开始数字
   结束数字”的形式。

   ###核心知识点
   * 字符串的切片操作，使用input().strip(0和input_list.split(",")实现
   * 集合的定义和使用，使用result set=set)定义集合，并使用result set..add0和result set.remove(0操作集合
   * 数字的判断和转换，使用if“"ini判断字符串是否包含“”，使用int((input().strip(O)和map(int,i.split(“-")》实现字符串转整数

## 解题代码

```python
# 去除首尾空白字符
input_str = input().strip()
request = int(input().strip())

# “，” 拆分
input_list = input_str.split(",")
result_set = set()

for i in input_list:
    # 判断是否包含 "-"
    if "-" in i:
        # 将 - 两端拆分转整型
        start,end = map(int,i.split("-"))
        # 遍历添加
        for j in range(start,end +1):
            result_set.add(j)
    else:
        # 单个字符直接添加
        result_set.add(int(i))

# 从列表中删除指定元素
result_set.remove(request)
# 转换为列表
result_list = list(result_set)
# 对其排序
result_list.sort()

# 确定起始
start = result_list[0]
last = start
output_list = []

# 从第二个元素开始遍历
for i in range(1,len(result_list)):
    cur = result_list[i]
    # 如果cur等于last的后序元素
    if cur == last +1:
        # 更新尾数
        last = cur
    else:
        # 否则将start到last的元素添加进output_list里面
        output_list.append((start,last))
        # 更新起始
        start = last = cur
# 把剩下的加入
output_list.append((start,last))

# 使用列表推导式构建一个字符串列表 output_str
# 并使用 ",".join(output_str) 方法以逗号为分隔符将其连接成一个字符串。
# 列表推导式会根据范围元组 (start, last) 是否相等，
# 使用不同的格式进行格式化
output_str =",".join(["{}-{}".format(i,j) if i!=j else "{}".format(i) for i,j in output_list])
print(output_str)
```

