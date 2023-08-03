#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def find_max_distance(parking):
    max_distance = 0  # 初始化最大距离为0
    empty = None  # 初始化空车位索引为空
    parking = [int(n) for n in parking.split(",")]

    for i, n in enumerate(parking):
        if n == 0:  
            # 计算该空车位与最近的已停车车辆之间的距离
            distance = min([abs(i - j) for j, x in enumerate(parking) if x == 1])
            if distance > max_distance:  # 如果该距离大于之前找到的最大距离
                max_distance = distance  # 更新最大距离的值
                empty_slot = i  # 更新空车位索引

    return max_distance


if __name__ == "__main__":
    parking = input() #请输入车位状态，以逗号分隔（1代表有车停，0代表空车位）：

    max_distance = find_max_distance(parking)
    print(max_distance)

