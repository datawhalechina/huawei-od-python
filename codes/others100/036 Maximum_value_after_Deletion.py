#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from collections import defaultdict

def solve_method(number):
    # 创建一个字典去统计数字频率
    number_count = defaultdict(int)
    res = []
    for c in number:
        # 相同的数字加一
        number_count[c] += 1
        res.append(c)

    for c, count in number_count.items():
        for i in range(len(res)):
            # 选择>=2的数
            if count < 2:
                break
            if res[i] == c:
                if res[i + 1] > c:
                    res.pop(i)
                    i -= 1
                    count -= 1
                elif i == len(res) - 1:
                    res.pop()
                    count -= 1

    return "".join(res)

if __name__ == "__main__":
    number = input().strip()
    print(solve_method(number))

