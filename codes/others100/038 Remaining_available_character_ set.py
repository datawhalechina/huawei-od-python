#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solve(n,m):
    # 拆分键值并保存
    def x_map(n):
        x_map = {}
        for i, j in list(map(lambda x: x.split(":"), n.split(","))):
            x_map[i] = int(j)
        return x_map
    
    
    total_map = x_map(total)
    used_map = x_map(used)
    for i in used_map.keys():
        diff = total_map[i] - used_map[i]
        if diff > 0:
            total_map[i] = diff
        else:
            total_map.pop(i)
    return (",".join(map(lambda x: ":".join(map(str, x)), total_map.items())))
if __name__ == '__main__':
    total, used = input().split("@")
    result = solve(total,used)
    print(result)

