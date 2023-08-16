#!/usr/bin/env python3
"""
@Author：Kaiwen Zuo
@File:Q52.py
@Date：2023/08/11 0:47
"""

def calculate_resp_time(T, M):
    # 如果M大于或等于128，则进行特定的位操作
    if M >= 128:
        # 提取M的位4-7，与0x10进行逻辑或操作，然后根据M的位0-2值左移
        M = ((M>>3) & 0xF| 0x10) << (M & 0x7 +3)

     # 返回T和新计算的M值的和
    return T+M
if __name__ == '__main__':

    C = int(input("Enter the number of test cases: "))
    # 使用列表推导式，对C个测试用例调用calculate_resp_time函数，并找到最小响应时间
    min_resp_time = min(calculate_resp_time(*map(int,input().split()))for _ in range (C))

    print("Minimum response time:", min_resp_time)  # 打印最小响应时间

