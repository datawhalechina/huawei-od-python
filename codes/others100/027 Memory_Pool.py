#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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

