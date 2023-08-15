#!/usr/bin/env python
# encoding: utf-8
"""
@author: LiYuHong
@file: 174_simple-memory-battery.py
@time: 2023/8/8 23:19
@project: huawei-od-python
@desc: 174 简易内存电池
"""


def solve_method(n, dis):
    class MemoryPool:
        def __init__(self):
            # 存储剩余的内存区间
            self.free_list = [(0, 99)]
            # 存储已经分配的内存区间
            self.memory = []

        def request(self, size):
            if size == 0:
                return "error"
            # 遍历整个可以选取的内存区间
            for i, (start, end) in enumerate(self.free_list):
                if end - start+1 >= size:
                    # 将合适的区间取出来，原列表内则删除掉
                    self.free_list.pop(i)
                    # 存放入已经分配的内存区间
                    self.memory.append((start, start+size-1))

                    # 如果该区间较大，分配完还有多余的空间
                    # 则将剩余切分完的区间再存入剩余的内存区间
                    if end - start+1 > size:
                        self.free_list.insert(i, (start + size, end))
                    return start
            return "error"

        def release(self, start):
            # 先找已分配的内存的首地址，是否有与start匹配的
            for ind, (l, r) in enumerate(self.memory):
                # 找到该区间后，从分配的memory中去掉，添加到未分配区间free_list中
                if l==start:
                    self.free_list.append(self.memory.pop(ind))
                    
                    # 区间之间有交集，我们要合并区间
                    stack = []
                    self.free_list.sort()
                    
                    for interval in self.free_list:
                        if stack and stack[-1][1]==interval[0]:
                            stack[-1][1]=interval[1]
                        stack.append(interval)
                    # 合并完成
                    self.free_list = stack
                    return None
            return "error"



    # -------------遍历请求------------
    result = []
    mp = MemoryPool()
    for i in range(n):
        cmd = dis[i].split('=')
        if cmd[0] == 'REQUEST':
            # 每一次请求的初始内存地址需要返回
            ans1 = mp.request(int(cmd[1]))
            result.append(ans1)
        else:
            ans2 = mp.release(int(cmd[1]))
            # 执行正确返回None即无返回值
            # 执行错误会返回 "error" 需要我们打印
            if ans2:
                result.append(ans2)
    return result
    

if __name__ == '__main__':
    assert solve_method(5, ['REQUEST=10', 'REQUEST=20','RELEASE=0','REQUEST=20','REQUEST=10']) == [0, 10, 30, 0]
    assert solve_method(2, ['REQUEST=10', 'REQUEST=20']) == [0, 10]
    assert solve_method(4, ['REQUEST=20', 'REQUEST=30', 'REQUEST=50', 'REQUEST=10']) == [0,20,50,'error']
    assert solve_method(4, ['REQUEST=10', 'REQUEST=20', 'RELEASE=0', 'RELEASE=0']) == [0,10,'error']

