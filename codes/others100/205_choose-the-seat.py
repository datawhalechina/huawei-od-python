#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 205_choose-the-seat.py
@time: 2023/7/21 10:40
@project: huawei-od-python
@desc: 205 选座位
"""


def solve_method(seatNum, seatOrLeave):
    order_seat = []
    # 已占用的座位
    used_seats = [False] * seatNum
    for i in range(len(seatOrLeave)):
        if seatOrLeave[i] > 0:
            available_seats = []
            for j in range(seatNum):
                if not used_seats[j]:
                    # 如果座位没有被占用，计算与左右两边相邻的空座位的距离
                    left_index, right_index = j, j
                    left_distance, right_distance = 0, 0
                    # 找到最左边的座位和距离
                    while left_index > 0 and not used_seats[left_index]:
                        left_distance += 1
                        left_index -= 1
                    # 找到最右边的座位和距离
                    while right_index < seatNum and not used_seats[right_index]:
                        right_distance += 1
                        right_index += 1
                    if not used_seats[0]:
                        # 最左边的第0号座位没有人坐
                        distance = left_distance + right_distance
                        distance_diff = -1
                    elif left_index >= 0 and not used_seats[seatNum - 1]:
                        # 最右边的座位没有人坐
                        distance = left_distance
                        distance_diff = -1
                    else:
                        distance = left_distance + right_distance
                        distance_diff = abs(left_distance - right_distance)

                    if j in [i for i in range(seatNum)
                                 if i not in order_seat and
                                    i not in [m + 1 for m in order_seat] and
                                    i not in [n - 1 for n in order_seat]]:
                        # 排除掉所有相邻的座位
                        available_seats.append([j, distance, distance_diff])

            # 按照左右距离和降序，按距离之差的绝对值升序（保证处于中间位置），座位号升序
            available_seats = sorted(available_seats, key=lambda x: (-x[1], x[2], x[0]))
            # 得到索引号最小的座位
            min_seat_index = available_seats[0][0]

            if len(available_seats) == 0:
                return -1
            used_seats[min_seat_index] = True
            order_seat.append(min_seat_index)
        else:
            used_seats[abs(seatOrLeave[i])] = False
            order_seat.remove(abs(seatOrLeave[i]))
        print(order_seat)
    return min_seat_index


if __name__ == '__main__':
    assert solve_method(10, [1, 1, 1, 1, -4, 1]) == 3
