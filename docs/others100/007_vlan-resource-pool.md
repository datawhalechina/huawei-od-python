# 007 VLAN资源池

## 题目描述

VLAN是一种为局域网设备进行逻辑划分的技术，为了标识不同的VLAN，引入了`vlan id`，取值范围是1\~4094之间的整数。

定义一个`vlan id`的资源池，资源池中连续的VLAN用`开始vlan-结束vlan`表示，不连续的用单个整数表示，所有的VLAN用`,`连接起来。

现有一个VLAN资源池，业务需要从资源池中申请一个`vlan`，需要你输出从VLAN资源池中移除申请的`vlan`后的资源池。

## 输入描述

第一行是字符串格式的VLAN资源池。

第二行是业务要申请的`vlan`，`vlan`的取值范围1\~4094。

## 输出描述

从输入vlan资源池中移除申请的vlan后，输出字符串格式的vlan资源池。输出要求满足题目中要求的格式，并且要求从小到大升序输出。

如果申请的`vlan`不在资源池，输出升序排序的原资源池的字符串即可。

## 示例描述

### 示例一

**输入：**
```text
1-5
2
```

**输出：**
```text
1,3-5
```

**说明：**  
原vlan资源池中有1、2、3、4、5，移除2后，剩下的1、3、4、5，按照升序排列的方式为`1 3-5`。

### 示例二

**输入：**

```text
20-21,15,18,30,5-10
15
```

**输出：**

```text
5-10,18,20-21,30
```

**说明：**  
原vlan资源池中有5、6、7、8、9、10、15、18、20、21、30，移除15后，剩下的为5、6、7、8、9、10、18、20、21、30，按照题目格式并升序后的结果为`5-10,18,20-21,30`。

### 示例三

**输入：**

```text
5,1-3
10
```

**输出：**

```text
1-3,5
```

**说明：**  
原资源池中有1、2、3、5，申请的资源不在资源池中，将原资源池升序输出，结果为`1-3,5`。

## 备注
输入池中vlan数量范围为2\~2094的整数，资源池中vlan不重复且合法，取值为1\~2094的整数，输入是乱序的。

## 解题思路

1. 根据原资源池，得到所有可用的vlan集合。
2. 在集合中删除申请的vlan。
3. 将剩下的资源按从小到大排序。
4. 使用元组形式，存储各段的始末vlan。
5. 按题目格式返回资源池的字符串。

## 解题代码

```python
def solve_method(pool, vlan_id):
    # 根据原资源池，得到所有可用的vlan集合
    pools = set()
    for vlan in pool:
        if "-" in vlan:
            vlan_seq = vlan.split("-")
            for i in range(int(vlan_seq[0]), int(vlan_seq[1]) + 1):
                pools.add(i)
        else:
            pools.add(int(vlan))

    # 删除申请的vlan
    if vlan_id in pools:
        pools.remove(vlan_id)

    # 将剩下的资源按从小到大排序
    pools = sorted(list(pools))

    # 得到各段的始末vlan
    result = []
    start_vlan = pools[0]
    end_vlan = start_vlan
    for i in range(1, len(pools)):
        cur_vlan = pools[i]
        if cur_vlan == end_vlan + 1:
            end_vlan = cur_vlan
        else:
            result.append((start_vlan, end_vlan))
            start_vlan = end_vlan = cur_vlan

    result.append((start_vlan, end_vlan))

    # 按题目格式输出资源池的字符串
    return [str(start) + "-" + str(end) if start != end else str(start) for start, end in result]


if __name__ == '__main__':
    assert solve_method(["1-5"], 2) == ["1", "3-5"]
    assert solve_method(["20-21", "15", "18", "30", "5-10"], 15) == ["5-10", "18", "20-21", "30"]
    assert solve_method(["5", "1-3"], 10) == ["1-3", "5"]
```

