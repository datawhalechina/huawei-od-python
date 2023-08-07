# 027 内存池

## 题目描述

有一个简易内存池，内存按照大小粒度分类，每个粒度有若干个可用内存资源。用户会进行一系列内存申请，需要按需分配内存池中的资源，返回申请结果成功失败列表。

分配规则如下:
1. 分配的内存要大于等于内存的申请量，存在满足需求的内存就必须分配，优先分配粒度小的，但内存不能拆分使用。
2. 需要按申请顺序分配，先申请的先分配，有可用内存分配则申请结果为`true`，没有可用则返回`false`。

注释：不考虑内存释放。

## 输入描述

输入为两行字符串:

第一行是内存池资源列表，包含内存粒度数据信息，粒度数据间用`,`分隔。 一个粒度信息内用`:`分隔，冒号前为内存粒度大小，冒号后为数量，资源列表不大于1024，每个粒度的数量不大于4096。

第二行是申请列表，申请的内存大小间用`,`分隔，申请列表不大于100000。

## 输出描述

输出为内存池分配结果。

## 示例描述

### 示例一

**输入：**

```text
64:2,128:1,32:4,1:128
50,36,64,128,121
```

**输出：**

```text
true,true,true,false,false
```

**说明：**

内存池资源包含: `64`内存共2个、`128`内存共1个、 `32`内存共4个、 `1`内存共128个的内存资源，针对`50,36,64,128,127`的内存申请序列，分配的内存依次是`64,64,128,null,null`。

第三次申请内存时已经将`128`内存分配出去，因此输出的结果是`true,true,true,false,false`。

## 解题思路

1. 构建内存池资源列表`memory_pool`，`key`为内存大小，`value`为可用数量。
2. 对内存池资源列表按照内存大小从小到大进行排序。   
3. 遍历申请列表，按照内存大小从小到大匹配内存资源列：
    - 如果匹配，返回`True`，可用数量减一。
    - 如果不匹配，返回`False`。
4. 返回所有内存分配结果。

## 解题代码

```Python
def solve_method(resources, jobs):
    memory_pool = {}
    result = []
    for resource in resources:
        split = resource.split(":")
        memory_pool[int(split[0])] = int(split[1])

    memory_pool = dict(sorted(memory_pool.items(), key=lambda x: x[0]))
    for job in jobs:
        allocation_done = False
        for size in memory_pool.keys():
            # 如果找到满足大小要求且数量大于零的内存资源，进行分配
            if size >= job and memory_pool[size] > 0:
                memory_pool[size] -= 1
                allocation_done = True
                result.append(True)
                break
            # 如果没有找到满足要求的内存资源，分配失败
        if not allocation_done:
            result.append(False)

    return result


if __name__ == '__main__':
    resources = ["64:2", "128:1", "32:4", "1:128"]
    jobs = [50, 36, 64, 128, 121]
    assert solve_method(resources, jobs) == [True, True, True, False, False]
```

