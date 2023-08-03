# 027 内存池

## 题目描述

有一个简易内存池，内存按照大小粒度分类，每个粒度有若干个可用内存资源。用户会进行一系列内存申请，需要按需分配内存池中的资源，返回申请结果成功失败列表。分配规则如下:

1. 分配的内存要大于等于内存的申请量存在满足需求的内存就必须分配优先分配粒度小的，但内存不能拆分使用

2. 需要按申请顺序分配先申请的先分配，有可用内存分配则申请结果为 `true`没有可用则返回 `false`

注释：不考虑内存释放

## 输入描述

输入为两行字符串:
第一行为内存池资源列表；
包含内存粒度数据信息，粒度数据间用逗号分割，
一个粒度信息内用冒号分割，冒号前为内存粒度大小，冒号后为数量，
资源列表不大于 `1024`
每个粒度的数量不大于 `4096`
第二行为申请列表，申请的内存大小间用逗号分割，申请列表不大千 `100000`
`50,36,64,128,127`

## 输出描述

输出为内存池分配结果
`true,true,true,false,false`

## 示例描述

### 示例一

**输入：**

```Plain Text
64:2,128:1,32:4,1:128
50,36,64,128,121
```

**输出：**

```Plain Text
true,true,true,false,false
```

**说明：**
内存池资源包含: `64k` 共`2`个、`128k` 共`1`个、 `32k` 共`4`个、 `1k` 共 `128` 个的内存资源针对 `50,36,64,128,127` 的内存申请序列，分配的内存依次是，`64,64,128,null,null`第三次申请内存时已经将 `128` 分配出去，因此输出的结果是`true, true ,true , false, false`

## 解题思路

**基本思路：** 根据题目可以模拟资源匹配过程

1. 首先对内存池资源列表进行处理，键为内存，值为可用数量

2. 遍历申请列表，匹配内存资源列表：
如果匹配，返回True，可用数量减一；如果不匹配，返回False

3. 返回结果。

## 解题代码

```Python
def memory(memory_pool, requests):
    # 将内存池资源列表转换为字典形式，键为内存，值为可用数量
    memory_pool = {int(k): int(v) for k, v in [x.split(":") for x in memory_pool.split(",")]}
    results = []
    # 遍历需求
    for request in requests:
        allocation_done = False
        for size in memory_pool.keys():
            # 如果找到满足大小要求且数量大于零的内存资源，进行分配
            if size >= request and memory_pool[size] > 0:
                memory_pool[size] -= 1
                allocation_done = True
                results.append(True)
                break
        # 如果没有找到满足要求的内存资源，分配失败
        if not allocation_done:
            results.append(False)

    return results

if __name__ == "__main__":
    memory_pool = input()
    requests = list(map(int, input().split(",")))
    results = memory(memory_pool, requests)
    print(",".join(map(str, results))) 
```

